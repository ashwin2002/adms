import sys
from PyQt5.QtWidgets import QAction, QApplication
from lib import logging, window

class SelectCompany:
    def __init__ (self, appObj, appConfig, windowObj, logger):
        self.appObj    = appObj
        self.appConfig = appConfig
        self.logger    = logger
        self.window    = windowObj
        return
