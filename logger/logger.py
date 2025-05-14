

class LoggerBase:

    def __init__(self):
        self._log = []

    def log(self, msg):
        self._log.append(msg)

class Logger(LoggerBase):

    def __init__(self):
        LoggerBase.__init__(self)

    def get_log(self):
        return self._log()