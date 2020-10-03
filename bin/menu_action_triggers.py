from models import fileUpload
from bin import jsonToExcel, txtToExcel, xlsx_parser, mail_from_excel


class MenuBarAction:
    def __init__(self, app_window, util_window, logger):
        self.appWindow = app_window
        self.window = util_window
        self.logger = logger
        return

    def show_about(self):
        self.logger.showDialogToUser('About', 'Version: 0.0',
                                     self.appWindow, 'about')

    def show_util_window(self):
        self.window.clearWidgets()
        self.appWindow.setCentralWidget(self.window)

    def json_to_excel(self, gstr_num):
        self.show_util_window()

        gstr_class = None
        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles(
            'Input Json Files', 'Json Files (*.json)', self.window)
        selected_file_num = len(selected_files)

        if gstr_num == 1:
            gstr_class = jsonToExcel.Gstr1
        elif gstr_num == 2:
            gstr_class = jsonToExcel.Gstr2

        json_converter_obj = gstr_class(file_upload_window.progressBar,
                                        file_upload_window.logViewer)

        if selected_file_num != 0:
            file_upload_window.filePercent = \
                int(file_upload_window.filePercent / 100)
        else:
            file_upload_window.logViewer.append('No Files to process')

        for jsonFile in selected_files:
            json_converter_obj.convert(jsonFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(
                file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
        del json_converter_obj
        return

    def txt_to_excel(self):
        self.show_util_window()

        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles(
            'Input Text Files', 'TXT Files (*.txt)', self.window)

        txt_file_converter_obj = txtToExcel.TextToExcel(
            file_upload_window.progressBar, file_upload_window.logViewer)
        for txtFile in selected_files:
            txt_file_converter_obj.convert(txtFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(
                file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
        del txt_file_converter_obj
        return

    def hsn_code_lookup(self):
        return

    def excel_parser(self):
        self.show_util_window()

        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles(
            'Input xlsx file', 'Xlsx (*.xlsx)', self.window)

        excel_parser = xlsx_parser.ExcelParser(file_upload_window.progressBar,
                                               file_upload_window.logViewer)
        for txtFile in selected_files:
            excel_parser.convert(txtFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(
                file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
        del excel_parser

    def send_mail_for_gstr_itc_data(self):
        self.show_util_window()

        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles(
            'Input xlsx file', 'Xlsx (*.xlsx)', self.window)

        excel_parser = mail_from_excel.MailFromExcel(
            file_upload_window.progressBar,
            file_upload_window.logViewer)
        for txtFile in selected_files:
            excel_parser.process(txtFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(
                file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
