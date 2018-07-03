from PyQt5 import QtWidgets

class VBox (QtWidgets.QVBoxLayout):
    def __init__ (self, parent=None):
        super (VBox, self).__init__ (parent)
        return

class ProgressBar (QtWidgets.QProgressBar):
    def __init__ (self, parent=None):
        super (ProgressBar, self).__init__ (parent=parent)
        return

class TextEdit (QtWidgets.QTextEdit):
    def __init__ (self, parent=None, readOnly=False):
        super (TextEdit, self).__init__ (parent=parent)
        self.setReadOnly (readOnly)
        return

    def clearText (self):
        self.clear ()
        return
