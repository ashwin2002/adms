from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, title, icon=None, **properties):
        super(MainWindow, self).__init__()
        self.menuBarObj = None
        self.toolBarObj = None
        self.statusBarObj = None
        self.setWindowTitle(title)
        if icon:
            self.setWindowIcon(QtGui.QIcon(icon))
        self.setProperties(**properties)

    def __del__(self):
        return

    def setProperties(self, **properties):
        for (key, value) in properties.items():
            if key == 'maximize':
                if value is True:
                    self.showMaximized()
                else:
                    self.showNormal()

    def createMenuBar(self):
        self.menuBarObj = self.menuBar()

    def createStatusBar(self):
        return

    def createToolBar(self):
        return


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent=parent)

    def clearWidgets(self):
        for child in (self.children()):
            try:
                child.destroy()
            except:
                pass

    def setProperties(self, **properties):
        for (win_property, value) in properties.items():
            if win_property == 'maximize':
                if value:
                    self.showMaximized()
                else:
                    self.showNormal()


class DockWidget(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super(DockWidget, self).__init__(parent=parent)


class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, title='Open File', filter='', parent=None):
        super(FileDialog, self).__init__(caption=title, filter=filter,
                                         parent=parent)
        self.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        self.setViewMode(QtWidgets.QFileDialog.Detail)

    def getSelectedFiles(self):
        selected_files = []
        if self.exec():
            selected_files = self.selectedFiles()
        return selected_files


class Popup(QtWidgets.QMessageBox):
    def __init__(self, popup_type, title, message, parent_window=None):
        popup_type = popup_type.lower()
        self.userChoice = None
        if popup_type == 'about':
            super(Popup, self).about(parent_window, title, message)
        elif popup_type == 'critical':
            super(Popup, self).critical(parent_window, title, message)
        elif popup_type == 'question':
            self.userChoice = super(Popup, self).question(parent_window, title,
                                                          message)
        elif popup_type == 'warning':
            super(Popup, self).warning(parent_window, title, message)
        else:
            super(Popup, self).information(parent_window, title, message)

    def getUserChoice(self):
        return self.userChoice
