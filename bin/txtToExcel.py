import traceback, os
import json, openpyxl
from lib import commonLib

class TextToExcel:
    def __init__ (self, progressBar, logViewer):
        self.prgressBar = progressBar
        self.logViewer  = logViewer
        return

    def logMsg (self, level, message):
        if level == 'ERROR':
            message = message.replace ('\n', '<br/>')
            (self.logViewer).append ('<font color="red">%s: %s</font>' % (level, message))
        elif level == 'WARNING':
            message = message.replace ('\n', '<br/>')
            (self.logViewer).append ('<font color="#e6ac00">%s: %s</font>' % (level, message))
        else:
            (self.logViewer).append ('%s: %s' % (level, message))
        return

    def checkFileExists (self, inputFileName, printError=True):
        errorCondition = False
        if not(os.path.isfile (inputFileName)):
            if printError:
                message = "File '%s' does not exists !" % (inputFileName)
                self.logMsg ('ERROR', message)
            errorCondition = True
        return errorCondition

    def appendRowToWorksheet (self, worksheetObj, dataRow):
        worksheetObj.append (dataRow)
        return

    def convert (self, inputFileName):
        self.logMsg ('INFO', "Processing file '%s'" % (inputFileName))
        outputFileName = inputFileName.split ('/')
        fileName = (outputFileName.pop()).split ('.')[0]
        if len(fileName) != 8:
            self.logMsg ('ERROR', "Invalid file name format '%s'. Use XXYY9999 format" % (fileName))
        else:
            compStr  = fileName[0:2]
            monthNum = int (fileName[4:6])
            yearNum  = int (fileName[6:8])
            dataTypeStr = fileName[2:4]
            outputFileName = '/'.join (outputFileName)
            outputFileName += '/%s_%s%d.xlsx' % (compStr, commonLib.getMonthStr (monthNum, 3), yearNum)

            fileNotExists = self.checkFileExists (outputFileName, printError=False)
            if fileNotExists:
                workbook  = openpyxl.Workbook ()
                workbook.guess_types = True
                worksheet = workbook.create_sheet (dataTypeStr)
            else:
                workbook = openpyxl.load_workbook (outputFileName)
                worksheetList = workbook.get_sheet_names ()

                if 'Sheet' in worksheetList:
                    worksheet = workbook.get_sheet_by_name ('Sheet')
                    workbook.remove_sheet (worksheet)

                if dataTypeStr in worksheetList:
                    worksheet = workbook.get_sheet_by_name (dataTypeStr)
                    workbook.remove_sheet (worksheet)

                worksheet = workbook.create_sheet (dataTypeStr)

        colDataDict = None
        try:
            with open (inputFileName, 'r') as filePtr:
                while True:
                    txtFileLine = filePtr.readline ()
                    if not(txtFileLine):
                        break

                    if txtFileLine.strip() == '':
                        continue

                    if not(colDataDict):
                        colDataDict = dict ()
                        charIndex = 0
                        inWord    = False
                        currWordIndex = -1
                        for char in txtFileLine:
                            if char == ' ' and inWord:
                                colDataDict[currWordIndex] = charIndex
                                inWord = False
                            elif char != ' ' and not(inWord):
                                inWord = True
                                currWordIndex = charIndex
                                colDataDict[charIndex] = -1
                            charIndex += 1
                        sortedDictKeys = sorted (colDataDict.keys())
                    else:
                        lineLen = len (txtFileLine)
                        xlDataRow = []
                        for startIndex in sortedDictKeys:
                            if lineLen < startIndex:
                                continue

                            data = (txtFileLine[startIndex:colDataDict[startIndex]]).strip()
                            try:
                                data = float(data)
                            except:
                                data = (txtFileLine[startIndex:colDataDict[startIndex]]).strip()
                            xlDataRow.append ((txtFileLine[startIndex:colDataDict[startIndex]]).strip())

                        self.appendRowToWorksheet (worksheet, xlDataRow)

            workbook.save (outputFileName)
        except Exception as e:
            self.logMsg ('ERROR', 'Exception during file parsing -> %s' % (traceback.format_exc()))

        self.logMsg ('INFO', "Output saved in file '%s'" % (outputFileName))
        self.logMsg ('::::::::::', 'Done ::::::::::')
        return
