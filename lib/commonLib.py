import os
import re
from models import fileUpload
from bin import jsonToExcel, txtToExcel, xlsx_parser


############ Common Class ################

class MenuBarAction:
    def __init__ (self, appWindow, utilWindow, logger):
        self.appWindow = appWindow
        self.window = utilWindow
        self.logger = logger
        return

    def showAbout (self):
        (self.logger).showDialogToUser ('About', 'Version: 0.0', self.appWindow, 'about')
        return

    def showUtilWindow (self):
        (self.window).clearWidgets ()
        (self.appWindow).setCentralWidget (self.window)
        return

    def jsonToExcel (self, gstrNum):
        self.showUtilWindow ()

        fileUploadWindow = fileUpload.FileUploader (self.window)
        selectedFiles    = fileUploadWindow.acceptInputFiles ('Input Json Files', 'Json Files (*.json)', self.window)
        selectedFileNum  = len(selectedFiles)

        if gstrNum == 1:
            jsonConverterObj = jsonToExcel.Gstr1 ((fileUploadWindow.progressBar), (fileUploadWindow.logViewer))
        elif gstrNum == 2:
            jsonConverterObj = jsonToExcel.Gstr2 ((fileUploadWindow.progressBar), (fileUploadWindow.logViewer))

        if selectedFileNum != 0:
            fileUploadWindow.filePercent = int((fileUploadWindow.filePercent) / 100)
        else:
            (fileUploadWindow.logViewer).append ('No Files to process')

        for jsonFile in selectedFiles:
            jsonConverterObj.convert (jsonFile)
            fileUploadWindow.totalPercent += (fileUploadWindow.filePercent)
            (fileUploadWindow.progressBar).setValue (fileUploadWindow.totalPercent)

        (fileUploadWindow.progressBar).setValue (100)
        fileUploadWindow.cleanUp ()
        del jsonConverterObj
        return

    def txtToExcel (self):
        self.showUtilWindow ()

        fileUploadWindow = fileUpload.FileUploader (self.window)
        selectedFiles    = fileUploadWindow.acceptInputFiles ('Input Text Files', 'TXT Files (*.txt)', self.window)
        selectedFileNum  = len(selectedFiles)

        txtFileConverterObj = txtToExcel.TextToExcel ((fileUploadWindow.progressBar), (fileUploadWindow.logViewer))
        for txtFile in selectedFiles:
            txtFileConverterObj.convert (txtFile)
            fileUploadWindow.totalPercent += (fileUploadWindow.filePercent)
            (fileUploadWindow.progressBar).setValue (fileUploadWindow.totalPercent)

        (fileUploadWindow.progressBar).setValue (100)
        fileUploadWindow.cleanUp ()
        del txtFileConverterObj
        return

    def hsnCodeLookup (self):
        return

    def excel_parser(self):
        self.showUtilWindow()

        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles('Input xlsx file', 'Xlsx (*.xlsx)', self.window)

        excel_parser = xlsx_parser.ExcelParser(file_upload_window.progressBar, file_upload_window.logViewer)
        for txtFile in selected_files:
            excel_parser.convert(txtFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
        del excel_parser

    def send_mail_for_gstr_itc_data(self):
        self.showUtilWindow()

        file_upload_window = fileUpload.FileUploader(self.window)
        selected_files = file_upload_window.acceptInputFiles('Input xlsx file', 'Xlsx (*.xlsx)', self.window)

        excel_parser = xlsx_parser.ExcelParser(file_upload_window.progressBar, file_upload_window.logViewer)
        for txtFile in selected_files:
            excel_parser.convert(txtFile)
            file_upload_window.totalPercent += file_upload_window.filePercent
            file_upload_window.progressBar.setValue(file_upload_window.totalPercent)

        file_upload_window.progressBar.setValue(100)
        file_upload_window.cleanUp()
        del excel_parser

############ Common Functions #################

def verifyGstinNo (gstin):
    gstin = re.search ('[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][0-9A-Z]{2}', gstin)
    if gstin:
        gstin = gstin.group(0)
    return gstin

def getMonthStr (monthNum, returnStrLen=-1):
    monthArr = []
    monthArr.append ('Invalid')
    monthArr.append ('January')
    monthArr.append ('Febuary')
    monthArr.append ('March')
    monthArr.append ('April')
    monthArr.append ('May')
    monthArr.append ('June')
    monthArr.append ('July')
    monthArr.append ('August')
    monthArr.append ('September')
    monthArr.append ('October')
    monthArr.append ('November')
    monthArr.append ('December')

    return monthArr[monthNum][0:returnStrLen]

def getStateList ():
    stateList = []
    stateList.append ('Jammu & Kashmir')    # 01
    stateList.append ('Himachal Pradesh')   # 02
    stateList.append ('Punjab')             # 03
    stateList.append ('Chandigarh')         # 04
    stateList.append ('Uttarakhand')        # 05
    stateList.append ('Haryana')            # 06
    stateList.append ('Delhi')              # 07
    stateList.append ('Rajasthan')          # 08
    stateList.append ('Uttar Pradesh')      # 09
    stateList.append ('Bihar')              # 10
    stateList.append ('Sikkim')             # 11
    stateList.append ('Arunachal Pradesh')  # 12
    stateList.append ('Nagaland')           # 13
    stateList.append ('Manipur')            # 14
    stateList.append ('Mizoram')            # 15
    stateList.append ('Tripura')            # 16
    stateList.append ('Meghalaya')          # 17
    stateList.append ('Assam')              # 18
    stateList.append ('West Bengal')        # 19
    stateList.append ('Jharkhand')          # 20
    stateList.append ('Orissa')             # 21
    stateList.append ('Chhattisgarh')       # 22
    stateList.append ('Madhya Pradesh')     # 23
    stateList.append ('Gujarat')            # 24
    stateList.append ('Daman & Diu')        # 25
    stateList.append ('Dadra & Nagar Haveli')   # 26
    stateList.append ('Maharashtra')    # 27
    stateList.append ('Andhra Pradesh') # 28
    stateList.append ('Karnataka')      # 29
    stateList.append ('Goa')            # 30
    stateList.append ('Lakshadweep')    # 31
    stateList.append ('Kerala')         # 32
    stateList.append ('Tamil Nadu')     # 33
    stateList.append ('Puducherry')     # 34
    stateList.append ('Andaman & Nicobar Islands')  # 35
    stateList.append ('Telangana')      # 36
    stateList.append ('Others')         # 37
    stateList.append ('')
    return stateList

def getStateCode (stateName):
    stateCode = '-1'
    stateName = stateName.strip()
    stateList = getStateList ()
    if stateName in stateList:
        stateCode = '%02d' % (stateList.index (stateName) + 1)
    return stateCode


def is_row_blank(d_row):
    for data in d_row:
        if data is not None:
            return False
    return True


def is_file_exists(input_file_name, logger=None):
    file_exists = True
    if not(os.path.isfile(input_file_name)):
        file_exists = False
        if logger:
            logger.error("File '%s' does not exists !" % input_file_name)
    return file_exists
