import os
import openpyxl
import traceback
from collections import OrderedDict

import constants
from constants.headers import ExcelHeaders


class ExcelParser:
    def __init__(self, progress_bar, log_viewer):
        self.progressBar = progress_bar
        self.logViewer = log_viewer

    @staticmethod
    def is_row_blank(data_row):
        for data in data_row:
            if data is not None:
                return False
        return True

    @staticmethod
    def get_excel_header(sheet_name):
        return getattr(getattr(constants, "headers"), sheet_name)

    def logMsg(self, level, message):
        if level == 'ERROR':
            message = message.replace('\n', '<br/>')
            self.logViewer.append('<font color="red">%s: %s</font>'
                                  % (level, message))
        elif level == 'WARNING':
            message = message.replace('\n', '<br/>')
            self.logViewer.append('<font color="#e6ac00">%s: %s</font>'
                                  % (level, message))
        else:
            self.logViewer.append('%s: %s' % (level, message))

    def check_file_exists(self, input_file_name, print_error=True):
        error_condition = False
        if not(os.path.isfile(input_file_name)):
            if print_error:
                message = "File '%s' does not exists !" % input_file_name
                self.logMsg('ERROR', message)
            error_condition = True
        return error_condition

    def extract_data_from_excel_sheet(self, input_sheet_name, input_sheet,
                                      row_num, dwnload_val, gst_2yrm_val):
        def get_month_abbr(month_num):
            return ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                    'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month_num]
        rows_to_append = list()
        num_of_blank_rows_to_break = 5
        num_blank_rows = 0

        sheet_header = ExcelHeaders.output_header[input_sheet_name]
        input_header = ExcelHeaders.input_header[input_sheet_name]

        t_header = self.get_excel_header(input_sheet_name)
        gstin_index = input_header.index(t_header.GSTIN)
        inv_num_index = input_header.index(t_header.INV_NO)
        while True:
            if num_blank_rows == num_of_blank_rows_to_break:
                break

            data_row = [None for _ in sheet_header]
            input_row = list()
            for index in range(len(sheet_header)):
                cell_val = input_sheet[chr(ord('A')+index)
                                       + str(row_num)].value
                input_row.append(cell_val)

            row_num += 1
            if ExcelParser.is_row_blank(input_row):
                num_blank_rows += 1
                continue

            num_blank_rows = 0
            gstin_val = input_row[gstin_index]
            if gstin_val is None or len(gstin_val) != 15 \
                    or input_row[inv_num_index].find("-Total") != -1:
                continue

            input_row[inv_num_index] = "=CONCATENATE(\"%s\")" \
                                       % input_row[inv_num_index]
            for index, d_type in enumerate(sheet_header):
                if d_type == t_header.DUMMY:
                    continue
                try:
                    d_index = input_header.index(d_type)
                    data_row[index] = input_row[d_index]
                except ValueError:
                    pass

            if t_header.INV_TYPE in sheet_header and data_row[
                    sheet_header.index(t_header.INV_TYPE)] == "R":
                data_row[sheet_header.index(t_header.INV_TYPE)] = "Regular"

            if t_header.INV_DATE in sheet_header:
                cell_val = \
                    data_row[sheet_header.index(t_header.INV_DATE)].split("-")
                cell_val.insert(1, get_month_abbr(int(cell_val.pop(1))))
                data_row[sheet_header.index(t_header.INV_DATE)] = \
                    "-".join(cell_val)

            if input_sheet_name == "B2B":
                d_index = sheet_header.index(t_header.ELIGIBLE)
                data_row.pop(d_index)
                data_row.insert(d_index, "Inputs")
                for d_type in [t_header.IGST_AVAILED,
                               t_header.CGST_AVAILED,
                               t_header.SGST_AVAILED,
                               t_header.CESS_AVAILED]:
                    d_index = sheet_header.index(d_type)
                    data_row.pop(d_index)
                    data_row.insert(d_index, 0.00)
                data_row[sheet_header.index(
                    t_header.DOWNLOAD)] = dwnload_val
                data_row[sheet_header.index(
                    t_header.GST2_YRM)] = gst_2yrm_val
            rows_to_append.append(data_row)
        return rows_to_append

    def shuffle_row_for_b2b_headers(self, input_sheet_name, rows_to_process,
                                    dwnload_val, gst_2yrm_val):
        def get_var_name(header_dict, value):
            for tem_header, t_val in header_dict.items():
                if t_val == value:
                    return tem_header
            return None

        index_map = list()
        rows_to_append = list()
        b2b_headers_class = constants.headers.B2B
        output_header = self.get_excel_header(input_sheet_name)

        for b2b_header in ExcelHeaders.output_header["B2B"]:
            b2b_header_var = get_var_name(b2b_headers_class.get_dict(),
                                          b2b_header)
            index = -1
            for t_index, t_header in enumerate(
                    ExcelHeaders.output_header[input_sheet_name]):
                target_header_var = get_var_name(output_header.get_dict(),
                                                 t_header)
                if b2b_header_var == target_header_var:
                    index = t_index
                    break
            index_map.append(index)

        for input_row in rows_to_process:
            row_data = list()
            for index in index_map:
                if index == -1:
                    row_data.append("")
                    continue
                row_data.append(input_row[index])
            row_data[ExcelHeaders.output_header["B2B"].index(
                b2b_headers_class.DOWNLOAD)] = dwnload_val
            row_data[ExcelHeaders.output_header["B2B"].index(
                b2b_headers_class.GST2_YRM)] = gst_2yrm_val

            d_index = ExcelHeaders.output_header["B2B"].index(
                b2b_headers_class.INV_TYPE)
            if input_sheet_name == "B2BA":
                row_data.pop(d_index)
                row_data.insert(d_index, input_sheet_name)
            if row_data[d_index].lower() == "credit note":
                for value_header in [b2b_headers_class.INV_VALUE,
                                     b2b_headers_class.TAXABLE,
                                     b2b_headers_class.IGST_PAID,
                                     b2b_headers_class.CGST_PAID,
                                     b2b_headers_class.SGST_PAID,
                                     b2b_headers_class.CESS_PAID]:
                    header_index = ExcelHeaders.output_header["B2B"].index(
                        value_header)
                    value = row_data.pop(header_index)
                    row_data.insert(header_index, -value)
            rows_to_append.append(row_data)
        return rows_to_append

    def convert(self, input_file_name):
        sheets_to_process = OrderedDict()
        sheets_to_process['B2B'] = dict()
        sheets_to_process['B2BA'] = dict()
        sheets_to_process['CDNR'] = dict()
        # sheets_to_process['CDNRA'] = dict()

        sheets_to_process['B2B']['start_row'] = 7
        sheets_to_process['B2BA']['start_row'] = 8
        sheets_to_process['CDNR']['start_row'] = 7
        # sheets_to_process['CDNRA']['start_row'] = 8

        self.logMsg('INFO', "Processing file '%s'" % input_file_name)
        output_file_name = input_file_name.split('/')
        file_name = (output_file_name.pop()).split('.')[0]
        output_file_name = '/'.join(output_file_name)
        output_file_name += '/%s_parsed.xlsx' % file_name
        file_not_exists = self.check_file_exists(output_file_name,
                                                 print_error=False)

        file_name_data = \
            input_file_name \
            .split("/")[-1] \
            .split('.')[0] \
            .split('_')
        gst_2yrm_val = file_name_data[1][2:] + file_name_data[1][0:2]
        dwnload_val = \
            str(file_name_data[3][0:2]) + '-' \
            + str(file_name_data[3][2:5]) + '-' \
            + str(file_name_data[3][5:])

        try:
            # Load input / output workbooks
            input_workbook = openpyxl.load_workbook(input_file_name)
            if file_not_exists:
                output_workbook = openpyxl.Workbook()
                output_workbook.guess_types = True
            else:
                output_workbook = openpyxl.load_workbook(input_file_name)

            output_workbook_sheets = output_workbook.get_sheet_names()

            for input_sheet_name in sheets_to_process.keys():
                if input_sheet_name not in input_workbook.get_sheet_names():
                    continue

                self.logMsg('INFO', 'Processing sheet %s' % input_sheet_name)
                if input_sheet_name in output_workbook_sheets:
                    self.logMsg('WARNING',
                                'Sheet %s already exists !! Will recreate..'
                                % input_sheet_name)
                    output_workbook.remove(
                        output_workbook.get_sheet_by_name(input_sheet_name))
                input_sheet = input_workbook.get_sheet_by_name(
                    input_sheet_name)

                # Start of data extraction logic
                rows_to_append = self.extract_data_from_excel_sheet(
                    input_sheet_name, input_sheet,
                    sheets_to_process[input_sheet_name]['start_row'],
                    dwnload_val, gst_2yrm_val)

                # Create and append data to output sheet
                output_sheet = output_workbook.create_sheet(input_sheet_name)
                output_sheet.append(
                    ExcelHeaders.output_header[input_sheet_name])
                for row in rows_to_append:
                    output_sheet.append(row)

                # Logic to append data to B2B sheet
                if input_sheet_name != "B2B":
                    rows_to_append = self.shuffle_row_for_b2b_headers(
                        input_sheet_name,
                        rows_to_append,
                        dwnload_val,
                        gst_2yrm_val)
                    output_sheet = output_workbook["B2B"]

                    for row in rows_to_append:
                        output_sheet.append(row)

            output_workbook.save(output_file_name)
        except Exception:
            self.logMsg('ERROR', 'Exception during file parsing -> %s'
                                 % (traceback.format_exc()))

        self.logMsg('INFO', "Output saved in file '%s'" % output_file_name)
        self.logMsg('::::::::::', 'Done ::::::::::')
