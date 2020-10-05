import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from data.input_misssing_mail import \
    html_header, html_footer, \
    msg_header, mail_msg, mail_subject, \
    tr_format, total_row_format
from data.mail import Info, Smtp
from lib.excel_lib import is_file_exists, is_row_blank
from lib.logging import UiLogger


class MailFromExcel:
    def __init__(self, progress_bar, log_viewer):
        self.progressBar = progress_bar
        self.log = UiLogger(log_viewer)
        return

    @staticmethod
    def insert_data(t_type, d_row, excel_data_dict):
        supp_name = d_row[6]
        supp_tin = d_row[7]
        # state = data_row[5]
        inv_no = d_row[3]
        inv_date = d_row[4]
        inv_val = d_row[8]
        taxable_val = d_row[9]
        igst_val = d_row[10]
        cgst_val = d_row[11]
        sgst_val = d_row[12]
        sno = d_row[0]

        if supp_name not in excel_data_dict[t_type].keys():
            excel_data_dict[t_type][supp_name] = dict()
            excel_data_dict[t_type][supp_name]["tin"] = supp_tin
            excel_data_dict[t_type][supp_name]["rows"] = list()

        excel_data_dict[t_type][supp_name]["rows"].append(
            [inv_no, inv_date, inv_val, taxable_val,
             igst_val, cgst_val, sgst_val, sno])

    def process(self, input_file_name):
        if not is_file_exists(input_file_name, logger=self.log):
            return

        self.log.info("Processing file %s" % input_file_name)
        input_workbook = openpyxl.load_workbook(input_file_name)
        file_name = input_file_name.split('\\')[-1].split('.')[0].split('_')
        company_initial = file_name[0]
        company_file_data = "%s %s - " % (company_initial, file_name[1])

        if company_initial not in Info.contact.keys() \
                or Info.contact[company_initial]["mail"] == "":
            print("Exiting: Mail id not defined for '%s'" % company_initial)
            exit(0)

        for input_sheet_name in input_workbook.get_sheet_names():
            if input_sheet_name != "PR":
                continue

            row_num = 0
            num_blank_rows = 0
            excel_data_dict = dict()
            excel_data_dict["itc_na"] = dict()
            excel_data_dict["gstr2_only"] = dict()
            process_sheet = False
            input_sheet = input_workbook.get_sheet_by_name(input_sheet_name)

            # Loop till finding first occurence of 'as per last Down' string
            while num_blank_rows < 5:
                row_num += 1
                data_row = list()
                for col in range(ord('A'), ord('Q')):
                    data_row.append(input_sheet[chr(col)+str(row_num)].value)

                if is_row_blank(data_row):
                    num_blank_rows += 1
                    continue

                num_blank_rows = 0
                if str(input_sheet['D%s' % row_num].value) \
                        == 'as per last Down':
                    process_sheet = True
                    break

            if not process_sheet:
                self.log.warning("Skipping sheet '%s'" % input_sheet_name)
                continue

            self.log.info("Processing sheet '%s'" % input_sheet_name)
            num_blank_rows = 0
            report_date = "NA.NA.NA.NA"
            gst_portal_line_found = False
            while num_blank_rows < 5:
                data_row = list()
                row_num += 1
                for col in range(ord('A'), ord('R')):
                    data_row.append(input_sheet[chr(col)+str(row_num)].value)

                if is_row_blank(data_row):
                    num_blank_rows += 1
                    continue

                # Reset num_blank_lines to continue reading excel sheet
                num_blank_rows = 0
                row_len = len(data_row)
                if row_len > 14 and data_row[14] == 'ITC-NA':
                    self.insert_data("itc_na", data_row, excel_data_dict)
                elif row_len >= 16 and data_row[16] \
                        == 'Available in GSTR-2 Only':
                    self.insert_data("gstr2_only", data_row, excel_data_dict)

                # Fetching date for GST_PORTAL data
                if gst_portal_line_found:
                    report_date = data_row[3]
                    print(report_date)

                if data_row[6] == "from GST Portal":
                    gst_portal_line_found = True
                else:
                    gst_portal_line_found = False

            report_date = "/".join(report_date.split(".")[1:])
            mail_count = 0
            for r_type, excel_data in excel_data_dict.items():
                smtp_session = None
                if excel_data.keys():
                    print("Connecting to server...")
                    smtp_session = smtplib.SMTP(Smtp.server, Smtp.port)
                    smtp_session.ehlo()
                    smtp_session.starttls()
                    smtp_session.ehlo()
                    smtp_session.login(Smtp.user_name, Smtp.password)
                    print("Login successful")

                comp_name = Info.contact[company_initial]["name"]
                curr_html_header = \
                    html_header % (msg_header[r_type] % comp_name,
                                   mail_msg[r_type])
                html_footer_comp_name = ""
                if r_type == "itc_na":
                    html_footer_comp_name = comp_name
                curr_html_footer = html_footer % (html_footer_comp_name,
                                                  report_date)
                total = 0
                for supp_name, supp_data in excel_data.items():
                    total += len(supp_data["rows"])
                    print("Sending mail for %s..." % supp_name)
                    msg = MIMEMultipart('alternative')
                    msg['From'] = Smtp.user_name
                    msg['To'] = Info.contact[company_initial]["mail"]
                    msg['Subject'] = "%s %s::%s - %s" \
                                     % (company_file_data,
                                        supp_name,
                                        supp_data["tin"],
                                        mail_subject[r_type])
                    total_igst = 0
                    total_cgst = 0
                    total_sgst = 0
                    mail_data = ""
                    for row in supp_data["rows"]:
                        row[0] = row[0].replace('=CONCATENATE("', '')
                        row[0] = row[0].rstrip('")')
                        mail_data += tr_format % tuple(row)
                        total_igst += float(row[4])
                        total_cgst += float(row[5])
                        total_sgst += float(row[6])

                    if len(supp_data["rows"]) > 1:
                        mail_data += total_row_format \
                                     % (total_igst, total_cgst, total_sgst)

                    data_payload = MIMEText(curr_html_header
                                            + mail_data
                                            + curr_html_footer,
                                            'html')
                    msg.set_payload(data_payload)
                    # msg.attach(data_to_attach)
                    smtp_session.sendmail(
                        Smtp.user_name,
                        Info.contact[company_initial]["mail"],
                        msg.as_string())
                    mail_count += 1

                    # Reconnect server for every 20 mails to avoid SPAM warning
                    if (mail_count % 20) == 0:
                        smtp_session.quit()
                        self.log.info("Re-connecting to server...")
                        smtp_session = smtplib.SMTP(Smtp.server, Smtp.port)
                        smtp_session.ehlo()
                        smtp_session.starttls()
                        smtp_session.ehlo()
                        smtp_session.login(Smtp.user_name, Smtp.password)
                        self.log.info("Login successful")

                # Exit smtp server
                if excel_data.keys():
                    smtp_session.quit()

                self.log.info("Total records for '%s': %s" % (r_type, total))

            self.log.info("Total emails send: %s" % mail_count)
