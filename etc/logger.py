from logging import Formatter, getLogger, StreamHandler, DEBUG, handlers

class Logger():
    def __init__(self, n=__name__):
        self.logger = getLogger(n)
        self.logger.setLevel(DEBUG)
        formatt = Formatter('%(asctime)s %(levelname)s - %(message)s')

        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

        handler = handlers.RotatingFileHandler(
            filename='.log',
            maxBytes=25545,
            backupCount=5
        )

        handler.setLevel(DEBUG)
        handler.setFormatter(formatt)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg, errmsg):
        self.logger.error(msg + ' [{}]'.format(errmsg))

    def critical(self, msg):
        self.logger.critical(msg)