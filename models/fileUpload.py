from lib import window, widgets

class FileUploader (object):
    def __init__ (self, windowObj):
        self.progressBar = None
        self.logViewer   = None
        self.filePercent = 100
        self.totalPercent = 0
        self.fileSelectDialog = None
        self.__createWidgets (windowObj)
        return

    def __createWidgets (self, windowObj):
        vboxObj = widgets.VBox (parent=windowObj)
        self.progressBar = widgets.ProgressBar (parent=windowObj)
        self.logViewer   = widgets.TextEdit (parent=windowObj)

        vboxObj.addWidget (self.progressBar)
        vboxObj.addWidget (self.logViewer)

        windowObj.setLayout (vboxObj)
        return

    def acceptInputFiles (self, winTitle, fileFilters, windowObj):
        self.fileSelectDialog = window.FileDialog (title=winTitle, filter=fileFilters, parent=windowObj)
        selectedFiles = (self.fileSelectDialog).getSelectedFiles ()

        filePercent  = 100
        totalPercent = 0

        (self.progressBar).setRange (0,100)
        (self.progressBar).setValue (0)
        return selectedFiles

    def cleanUp (self):
        if self.fileSelectDialog:
            del self.fileSelectDialog
        return
