import configparser
import os
import sys
from PyQt5.QtWidgets import QAction, QApplication

from bin.menu_action_triggers import MenuBarAction
from resources import appConfig
from lib import window, osFunctions, logging


class Application (QApplication):
    def __init__ (self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.appWindow  = None
        self.mainWindow = None
        self.utilWindow = None
        self.settings = None
        self.logger   = None
        self.menuActions = None
        return

    def validateSettingsFile (self, settingsFile):
        (self.settings).read (settingsFile)
        configSections = (self.settings).sections ()

        if 'log' in configSections:
            value = (self.settings)['log'].get ('path')
            if not(value) or value == '':
                (self.settings)['log']['path'] = 'logs'
        else:
            (self.settings).add_section ('log')
            (self.settings)['log']['path'] = 'logs'

        if 'data' in configSections:
            value = (self.settings)['data'].get ('path')
            if not(value) or value == '':
                (self.settings)['data']['path'] = 'data'
        else:
            (self.settings).add_section ('data')
            (self.settings)['data']['path'] = 'data'

        with open (settingsFile, 'w') as filePtr:
            (self.settings).write (filePtr)
        return

    def createMenuBar (self):
        (self.appWindow).createMenuBar ()

        ### Create Menu bar items ###
        menuBar = (self.appWindow).menuBarObj
        fileMenu   = menuBar.addMenu ('&File')
        optionMenu = menuBar.addMenu ('&Options')
        utilsMenu  = menuBar.addMenu ('&Utilities')
        adminMenu  = menuBar.addMenu ('&Admin')
        helpMenu   = menuBar.addMenu ('&Help')

        jsonToXlMenu = utilsMenu.addMenu ('&Json To Excel')

        ### Create Add option to Menu bar items ###
        gstr1JsonToXlAction = QAction ('GSTR &1', (self.appWindow))
        gstr2JsonToXlAction = QAction ('GSTR &2', (self.appWindow))
        txtToExcelAction    = QAction ('&Text To Excel', (self.appWindow))
        excel_parser_action = QAction('Parse E&xcel', self.appWindow)
        send_mail_from_excel = QAction('&Send mail', self.appWindow)
        #hsnCodeLookup = QAction ('&HSN Lookup', (self.appWindow))

        jsonToXlMenu.addAction (gstr1JsonToXlAction)
        jsonToXlMenu.addAction (gstr2JsonToXlAction)
        utilsMenu.addAction (send_mail_from_excel)
        utilsMenu.addAction (txtToExcelAction)
        utilsMenu.addAction(excel_parser_action)
        #utilsMenu.addAction (hsnCodeLookup)

        aboutAction = QAction ('&About', (self.appWindow))
        helpMenu.addAction (aboutAction)

        menuExitAction = QAction ('E&xit', (self.appWindow))
        menuExitAction.setShortcut ('Ctrl+Q')
        fileMenu.addAction (menuExitAction)

        ### Register Event handlers for menu items ###
        aboutAction.triggered.connect(self.menuActions.show_about)
        menuExitAction.triggered.connect(self.quit)
        gstr1JsonToXlAction.triggered.connect(lambda: self.menuActions.json_to_excel(1))
        gstr2JsonToXlAction.triggered.connect(lambda: self.menuActions.json_to_excel(2))
        txtToExcelAction.triggered.connect(self.menuActions.txt_to_excel)
        excel_parser_action.triggered.connect(self.menuActions.excel_parser)
        send_mail_from_excel.triggered.connect(
            self.menuActions.send_mail_for_gstr_itc_data)
        #(hsnCodeLookup.triggered).connect (self.menuActions.hsn_code_lookup)

    def loadBasicUI (self):
        self.appWindow   = window.MainWindow ('ADMS', icon='icons/icon.png', maximize=True)
        self.mainWindow  = window.Window (parent=self.appWindow)
        self.utilWindow  = window.Window (parent=self.appWindow)
        self.menuActions = MenuBarAction (self.appWindow, self.utilWindow, self.logger)
        (self.appWindow).setCentralWidget (self.mainWindow)
        self.createMenuBar ()
        sys.exit(self.exec())

    def verifyFiles (self):
        if not(os.path.isfile (appConfig.settingFileName)):
            with open (appConfig.settingFileName, 'w') as filePtr:
                pass
            #window.Popup ('critical', 'File Missing!', 'File \'%s\' missing' % (appConfig.settingFileName))
            #sys.exit (1)

    def run (self):
        self.settings = configparser.ConfigParser ()
        self.validateSettingsFile (appConfig.settingFileName)

        osFunctions.createDir ([(self.settings)['log']['path'], (self.settings)['data']['path']])

        self.logger = logging.Logger ((self.settings)['log']['path'], 'debug.log')
        self.logger.openLogFile()
        self.loadBasicUI()


if __name__ == '__main__':
    applicationObj = Application(sys.argv)
    applicationObj.verifyFiles()
    applicationObj.run()
