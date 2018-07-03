import time
from lib.window import Popup

class Logger:
    def __init__ (self, sysPath, logFileName, activeUser='Guest'):
        self.sysPath = sysPath
        self.logFileName = sysPath + '\\' + logFileName
        activeUser    = 'Guest'
        logFileHandle = None
        return

    def selfDestroy (self):
        self.logMsg ('INFO', 'Destroying ' + self.__class__.__name__ + ' class')
        self.closeLogFile ()
        del self
        return

    def setActiveUser (self, uName):
        self.activeUser = uName
        return

    def openLogFile (self):
        self.logFileHandle = open (self.logFileName, 'a')
        return

    def closeLogFile (self):
        if self.logFileHandle:
            self.logFileHandle.close ()
            self.logFileHandle = None
        return

    def logMsg (self, level, message):
        if (self.logFileHandle):
            currTime = time.strftime ('%d/%m/%Y %X ')
            self.logFileHandle.write (currTime + '(' + self.activeUser + ') ' + level + ' : ' + message + '\n')
        return

    def showDialogToUser (self, title, message, parentWindow=None, dialogType='INFO'):
        dialog = Popup (dialogType, title, message, parentWindow)
        return
