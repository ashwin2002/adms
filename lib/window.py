from PyQt5 import QtWidgets, QtGui

class MainWindow (QtWidgets.QMainWindow):
    def __init__ (self, title, icon=None, **properties):
        super (MainWindow, self).__init__ ()
        self.menuBarObj = None
        self.toolBarObj = None
        self.statusBarObj = None
        self.setWindowTitle (title)
        if icon:
            self.setWindowIcon (QtGui.QIcon (icon))
        self.setProperties (**properties)
        return

    def __del__ (self):
        return

    def setProperties (self, **properties):
        for (key, value) in properties.items():
            if key == 'maximize':
                if value == True:
                    self.showMaximized ()
                else:
                    self.showNormal ()
        return

    def createMenuBar (self):
        self.menuBarObj = self.menuBar ()
        return

    def createStatusBar (self):
        return

    def createToolBar (self):
        return

class Window (QtWidgets.QWidget):
    def __init__ (self, parent=None):
        super (Window, self).__init__ (parent=parent)
        return

    def clearWidgets (self):
        for child in (self.children ()):
            try:
                child.destroy ()
            except:
                pass
        return

    def setProperties (self, **properties):
        for (property, value) in properties.items ():
            if property == 'maximize':
                if value:
                    self.showMaximized ()
                else:
                    self.showNormal ()
        return

class DockWidget (QtWidgets.QDockWidget):
    def __init__ (self, parent=None):
        super (DockWidget, self).__init__ (parent=parent)
        return

class FileDialog (QtWidgets.QFileDialog):
    def __init__ (self, title='Open File', filter='', parent=None):
        super (FileDialog, self).__init__ (caption=title, filter=filter, parent=parent)
        self.setFileMode (QtWidgets.QFileDialog.ExistingFiles)
        self.setViewMode (QtWidgets.QFileDialog.Detail)
        return

    def getSelectedFiles (self):
        selectedFiles = []
        if (self.exec()):
            selectedFiles = self.selectedFiles ()
        return selectedFiles

class Popup (QtWidgets.QMessageBox):
    def __init__ (self, type, title, message, parent_window=None):
        type = type.lower()
        self.userChoice = None
        if type == 'about':
            super (Popup, self).about (parent_window, title, message)
        elif type == 'critical':
            super (Popup, self).critical (parent_window, title, message)
        elif type == 'question':
            self.userChoice = super (Popup, self).question (parent_window, title, message)
        elif type == 'warning':
            super (Popup, self).warning (parent_window, title, message)
        else:
            super (Popup, self).information (parent_window, title, message)
        return

    def getUserChoice (self):
        return self.userChoice
