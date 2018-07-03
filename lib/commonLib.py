import re
from lib import window, widgets
from models import fileUpload
from bin import jsonToExcel, txtToExcel

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
    '''
        Customer State code data:
        01	JAMMU & KASHMIR
        02	HIMACHAL PRADESH
        03	PUNJAB
        04	CHANDIGARH
        05	UTTARAKHAND
        06	HARYANA
        07	DELHI
        08	RAJASTHAN
        09	UTTAR PRADESH
        10	BIHAR
        11	SIKKIM
        12	ARUNACHAL PRADESH
        13	NAGALAND
        14	MANIPUR
        15	MIZORAM
        16	TRIPURA
        17	MEGHALAYA
        18	ASSAM
        19	WEST BENGAL
        20	JHARKHAND
        21	ORISSA
        22	CHHATTISGARH
        23	MADHYA PRADESH
        24	GUNJARAT
        25	DAMAN & DIU
        26	DADRA & NAGAR HAVELI
        27	MAHARASHTRA
        28	ANDHRA PRADESH
        29	KARNATAKA
        30	GOA
        31	LAKSHADWEEP
        32	KERALA
        33	TAMIL NADU
        34	PUDUCHERRY
        35	ANDAMAN & NICOBAR ISLANDS
        36	TELANGANA
    '''

    stateList = []
    stateList.append ('Jammu & Kashmir')
    stateList.append ('Himachal Pradesh')
    stateList.append ('Punjab')
    stateList.append ('Chandigarh')
    stateList.append ('Uttarakhand')
    stateList.append ('Haryana')
    stateList.append ('Delhi')
    stateList.append ('Rajasthan')
    stateList.append ('Uttar Pradesh')
    stateList.append ('Bihar')
    stateList.append ('Sikkim')
    stateList.append ('Arunachal Pradesh')
    stateList.append ('Nagaland')
    stateList.append ('Manipur')
    stateList.append ('Mizoram')
    stateList.append ('Tripura')
    stateList.append ('Meghalaya')
    stateList.append ('Assam')
    stateList.append ('West Bengal')
    stateList.append ('Jharkhand')
    stateList.append ('Orissa')
    stateList.append ('Chhattisgarh')
    stateList.append ('Madhya Pradesh')
    stateList.append ('Gujarat')
    stateList.append ('Daman & Diu')
    stateList.append ('Dadra & Nagar Haveli')
    stateList.append ('Maharashtra')
    stateList.append ('Andhra Pradesh')
    stateList.append ('Karnataka')
    stateList.append ('Goa')
    stateList.append ('Lakshadweep')
    stateList.append ('Kerala')
    stateList.append ('Tamil Nadu')
    stateList.append ('Puducherry')
    stateList.append ('Andaman & Nicobar Islands')
    stateList.append ('Telangana')
    stateList.append ('')
    stateList.append ('')
    return stateList

def getStateCode (stateName):
    stateCode = '-1'
    stateName = stateName.strip()
    stateList = getStateList ()
    if stateName in stateList:
        stateCode = '%02d' % (stateList.index (stateName) + 1)
    return stateCode
