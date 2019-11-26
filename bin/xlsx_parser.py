import os
import openpyxl
import traceback


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

    def logMsg(self, level, message):
        if level == 'ERROR':
            message = message.replace('\n', '<br/>')
            self.logViewer.append('<font color="red">%s: %s</font>' % (level, message))
        elif level == 'WARNING':
            message = message.replace('\n', '<br/>')
            self.logViewer.append('<font color="#e6ac00">%s: %s</font>' % (level, message))
        else:
            self.logViewer.append('%s: %s' % (level, message))

    def checkFileExists(self, input_file_name, print_error=True):
        error_condition = False
        if not(os.path.isfile(input_file_name)):
            if print_error:
                message = "File '%s' does not exists !" % input_file_name
                self.logMsg('ERROR', message)
            error_condition = True
        return error_condition

    def appendRowToWorksheet(self, worksheet_obj, data_row):
        worksheet_obj.append(data_row)

    def convert(self, input_file_name):
        sheets_to_process = dict()
        sheets_to_process['B2B'] = dict()
        sheets_to_process['B2BA'] = dict()
        sheets_to_process['CDNR'] = dict()
        sheets_to_process['CDNRA'] = dict()
        sheets_to_process['B2B']['check_dup_row'] = False
        sheets_to_process['B2BA']['check_dup_row'] = False
        sheets_to_process['CDNR']['check_dup_row'] = True
        sheets_to_process['CDNRA']['check_dup_row'] = True
        sheets_to_process['B2B']['header'] = ['GSTIN', 'INV No', 'INV Date', 'INV Value',
                                              'Place', 'RCM', 'Rate', 'Taxable', 'IGST Paid',
                                              'CGST Paid', 'SGST Paid', 'CESS Paid',
                                              'Eligible', 'IGST availed', 'CGST availed',
                                              'SGST availed', 'CESS availed', 'Download date',
                                              'GST2YRM', 'Submited']
        sheets_to_process['B2BA']['header'] = ['GSTIN', 'SUPPNAME', 'INV No', 'INV Date',
                                               '', '', 'INV Value', 'Place', 'RCM',
                                               'INV Type', 'Rate', 'Taxable', 'IGST', 'CGST',
                                               'SGST', 'CESS', 'IGST availed', 'CGST availed',
                                               'SGST availed', 'CESS availed', 'Download date',
                                               'GST2YRM', 'Submitted']
        sheets_to_process['CDNR']['header'] = ['GSTIN', 'SUPP Name', 'Note Type', 'INV No',
                                               'INV date', 'INV value', 'Reason', 'Rate',
                                               'Taxable', 'IGST Paid', 'CGST Paid', 'SGST Paid',
                                               'CESS Paid', 'Submitted']
        sheets_to_process['CDNRA']['header'] = ['GSTIN', 'SUPP Name', 'Note Type', 'INV No',
                                                'INV date', '', '', '', 'INV value', 'Place',
                                                '', 'Rate',
                                                'Taxable', 'IGST Paid', 'CGST Paid', 'SGST Paid',
                                                'Submitted']
        sheets_to_process['B2B']['start_row'] = 4
        sheets_to_process['B2BA']['start_row'] = 5
        sheets_to_process['CDNR']['start_row'] = 11
        sheets_to_process['CDNRA']['start_row'] = 10
        sheets_to_process['B2B']['end_col'] = 'V'
        sheets_to_process['B2BA']['end_col'] = 'W'
        sheets_to_process['CDNR']['end_col'] = 'T'
        sheets_to_process['CDNRA']['end_col'] = 'Q'
        num_of_blank_rows_to_break = 5

        self.logMsg('INFO', "Processing file '%s'" % input_file_name)
        output_file_name = input_file_name.split('/')
        file_name = (output_file_name.pop()).split('.')[0]
        output_file_name = '/'.join(output_file_name)
        output_file_name += '/%s_parsed.xlsx' % file_name
        file_not_exists = self.checkFileExists(output_file_name, print_error=False)

        try:
            # Load input / output workbooks
            input_workbook = openpyxl.load_workbook(input_file_name)
            if file_not_exists:
                output_workbook = openpyxl.Workbook()
                output_workbook.guess_types = True
            else:
                output_workbook = openpyxl.load_workbook(input_file_name)

            output_workbook_sheets = output_workbook.get_sheet_names()

            for input_sheet_name in input_workbook.get_sheet_names():
                if input_sheet_name in sheets_to_process.keys():
                    self.logMsg('INFO', 'Processing sheet %s' % input_sheet_name)
                    if input_sheet_name in output_workbook_sheets:
                        self.logMsg('WARNING', 'Sheet %s already exists !! Will recreate..'
                                               % input_sheet_name)
                        output_workbook.remove(output_workbook.get_sheet_by_name(input_sheet_name))
                    input_sheet = input_workbook.get_sheet_by_name(input_sheet_name)
                    output_sheet = output_workbook.create_sheet(input_sheet_name)
                    row_num = sheets_to_process[input_sheet_name]['start_row']
                    num_blank_rows = 0
                    prev_row = []

                    self.appendRowToWorksheet(output_sheet, sheets_to_process[input_sheet_name]['header'])
                    col_range = [chr(i) for i in range(ord('A'), ord(sheets_to_process[input_sheet_name]['end_col'])+1)]
                    while True:
                        data_row = list()
                        for col in col_range:
                            data_row.append(input_sheet[col + str(row_num)].value)

                        if ExcelParser.is_row_blank(data_row):
                            num_blank_rows += 1
                        else:
                            num_blank_rows = 0
                            if len(data_row[0]) == 15:
                                if sheets_to_process[input_sheet_name]['check_dup_row']:
                                    if not prev_row \
                                            or prev_row[0] != data_row[0]\
                                            or prev_row[8] != data_row[8]:
                                        self.appendRowToWorksheet(output_sheet, data_row)
                                        prev_row = data_row
                                else:
                                    self.appendRowToWorksheet(output_sheet, data_row)

                        if num_blank_rows == num_of_blank_rows_to_break:
                            break
                        row_num += 1

            output_workbook.save(output_file_name)
        except Exception as e:
            self.logMsg('ERROR', 'Exception during file parsing -> %s' % (traceback.format_exc()))

        self.logMsg('INFO', "Output saved in file '%s'" % output_file_name)
        self.logMsg('::::::::::', 'Done ::::::::::')
