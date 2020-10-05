import time
from lib.window import Popup


class FileLogger:
    def __init__(self, sys_path, log_file_name, active_user='Guest'):
        self.sysPath = sys_path
        self.logFileName = sys_path + '\\' + log_file_name
        self.activeUser = active_user
        self.logFileHandle = None

    def selfDestroy(self):
        self.log_msg('INFO', 'Destroying ' + self.__class__.__name__ + ' class')
        self.close_log_file()
        del self

    def setActiveUser(self, u_name):
        self.activeUser = u_name

    def open_log_file(self):
        self.logFileHandle = open(self.logFileName, 'a')

    def close_log_file(self):
        if self.logFileHandle:
            self.logFileHandle.close()
            self.logFileHandle = None

    def log_msg(self, level, message):
        if self.logFileHandle:
            curr_time = time.strftime('%d/%m/%Y %X ')
            self.logFileHandle.write(curr_time + '(' + self.activeUser + ') '
                                     + level + ' : ' + message + '\n')

    def showDialogToUser(self, title, message,
                         parent_window=None, dialog_type='INFO'):
        _ = Popup(dialog_type, title, message, parent_window)


class UiLogger(object):
    def __init__(self, log_viewer):
        self.log_viewer = log_viewer

    def info(self, message):
        self.log_viewer.append('INFO: %s' % message)

    def error(self, message):
        message = message.replace('\n', '<br/>')
        self.log_viewer.append('<font color="red">ERROR: %s</font>' % message)

    def warning(self, message):
        message = message.replace('\n', '<br/>')
        self.log_viewer.append('<font color="#e6ac00">WARNING: %s</font>'
                               % message)

    def raw_line(self, message):
        self.log_viewer.append(message)
