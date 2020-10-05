import configparser
import os
import sys
from PyQt5.QtWidgets import QAction, QApplication

from bin.menu_action_triggers import MenuBarAction
from resources import appConfig
from lib import window, osFunctions, logging


class Application (QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.appWindow = None
        self.mainWindow = None
        self.utilWindow = None
        self.settings = None
        self.logger = None
        self.menuActions = None

    def validate_settings_file(self, settings_file):
        self.settings.read(settings_file)
        config_sections = self.settings.sections()

        if 'log' in config_sections:
            value = self.settings['log'].get('path')
            if not value or value == '':
                self.settings['log']['path'] = 'logs'
        else:
            self.settings.add_section('log')
            self.settings['log']['path'] = 'logs'

        if 'data' in config_sections:
            value = self.settings['data'].get('path')
            if not value or value == '':
                self.settings['data']['path'] = 'data'
        else:
            self.settings.add_section('data')
            self.settings['data']['path'] = 'data'

        with open(settings_file, 'w') as filePtr:
            self.settings.write(filePtr)

    def create_menu_bar(self):
        self.appWindow.createMenuBar()

        # Create Menu bar items
        menu_bar = self.appWindow.menuBarObj
        file_menu = menu_bar.addMenu('&File')
        # option_menu = menu_bar.addMenu('&Options')
        utils_menu = menu_bar.addMenu('&Utilities')
        # admin_menu = menu_bar.addMenu('&Admin')
        help_menu = menu_bar.addMenu('&Help')

        json_to_xl_menu = utils_menu.addMenu('&Json To Excel')
        parse_excel_menu = utils_menu.addMenu('Parse E&xcel')

        # Create Add option to Menu bar items
        gstr1_json_to_xl_action = QAction('GSTR &1', self.appWindow)
        gstr2_json_to_xl_action = QAction('GSTR &2', self.appWindow)
        txt_to_excel_action = QAction('&Text To Excel', self.appWindow)
        extract_data_action = QAction('E&xtract data', self.appWindow)
        extract_gstr2b_action = QAction('Extract &Gstr-2B data',
                                        self.appWindow)
        send_mail_action = QAction('Send &mail', self.appWindow)
        # hsnCodeLookup = QAction ('&HSN Lookup', (self.appWindow))

        json_to_xl_menu.addAction(gstr1_json_to_xl_action)
        json_to_xl_menu.addAction(gstr2_json_to_xl_action)
        parse_excel_menu.addAction(extract_data_action)
        parse_excel_menu.addAction(extract_gstr2b_action)
        parse_excel_menu.addAction(send_mail_action)
        utils_menu.addAction(txt_to_excel_action)
        # utilsMenu.addAction (hsnCodeLookup)

        about_action = QAction('&About', self.appWindow)
        help_menu.addAction(about_action)

        menu_exit_action = QAction('E&xit', self.appWindow)
        menu_exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(menu_exit_action)

        # Register Event handlers for menu items
        about_action.triggered.connect(self.menuActions.show_about)
        menu_exit_action.triggered.connect(self.quit)
        gstr1_json_to_xl_action.triggered.connect(
            lambda: self.menuActions.json_to_excel(1))
        gstr2_json_to_xl_action.triggered.connect(
            lambda: self.menuActions.json_to_excel(2))
        txt_to_excel_action.triggered.connect(self.menuActions.txt_to_excel)
        extract_data_action.triggered.connect(self.menuActions.excel_parser)
        extract_gstr2b_action.triggered.connect(
            self.menuActions.extract_gstr2b)
        send_mail_action.triggered.connect(
            self.menuActions.send_mail_for_gstr_itc_data)
        # hsnCodeLookup.triggered.connect(self.menuActions.hsn_code_lookup)

    def load_basic_ui(self):
        self.appWindow = window.MainWindow('ADMS', icon='icons/icon.png',
                                           maximize=True)
        self.mainWindow = window.Window(parent=self.appWindow)
        self.utilWindow = window.Window(parent=self.appWindow)
        self.menuActions = MenuBarAction(self.appWindow, self.utilWindow,
                                         self.logger)
        self.appWindow.setCentralWidget(self.mainWindow)
        self.create_menu_bar()
        sys.exit(self.exec())

    @staticmethod
    def verify_files():
        if not os.path.isfile(appConfig.settingFileName):
            with open(appConfig.settingFileName, 'w') as _:
                pass
            # window.Popup('critical', 'File Missing!',
            #              'File \'%s\' missing' % appConfig.settingFileName)
            # sys.exit (1)

    def run(self):
        self.settings = configparser.ConfigParser()
        self.validate_settings_file(appConfig.settingFileName)

        osFunctions.create_dir([self.settings['log']['path'],
                                self.settings['data']['path']])

        self.logger = logging.FileLogger(self.settings['log']['path'],
                                         'debug.log')
        self.logger.open_log_file()
        self.load_basic_ui()


if __name__ == '__main__':
    applicationObj = Application(sys.argv)
    applicationObj.verify_files()
    applicationObj.run()
