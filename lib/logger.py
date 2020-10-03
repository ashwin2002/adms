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
