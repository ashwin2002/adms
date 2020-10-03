from lib import window, widgets


class FileUploader(object):
    def __init__(self, window_obj):
        self.progressBar = None
        self.logViewer = None
        self.filePercent = 100
        self.totalPercent = 0
        self.fileSelectDialog = None
        self.__createWidgets(window_obj)

    def __createWidgets(self, window_obj):
        vbox_obj = widgets.VBox(parent=window_obj)
        self.progressBar = widgets.ProgressBar(parent=window_obj)
        self.logViewer = widgets.TextEdit(parent=window_obj)

        vbox_obj.addWidget(self.progressBar)
        vbox_obj.addWidget(self.logViewer)

        window_obj.setLayout(vbox_obj)

    def acceptInputFiles(self, win_title, file_filters, window_obj):
        self.fileSelectDialog = window.FileDialog(title=win_title,
                                                  filter=file_filters,
                                                  parent=window_obj)
        selected_files = self.fileSelectDialog.getSelectedFiles()

        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)
        return selected_files

    def cleanUp(self):
        if self.fileSelectDialog:
            del self.fileSelectDialog
