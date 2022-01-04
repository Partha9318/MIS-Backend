import logging
import os

class Logger:
    
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)


    formatter = logging.Formatter('%(lineno)s:::%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    file_handler = logging.FileHandler('log_final.log')
    file_handler.setFormatter(formatter)

    def add_handler(self):
        return self.logger.addHandler(self.file_handler)

class Message(Logger):
    def __init__(self, name):
        super().__init__(name)

    def debug(self, message):
        return self.logger.debug(message)

    def info(self, message):
        return self.logger.info(message)

    def warning(self, message):
        return self.logger.warning(message)

    def error(self, message):
        return self.logger.exception(message)

    def critical(self, message):
        return self.logger.critical(message)

name = os.path.basename(__name__)
filename = 'all_logs1.log'
logger = Logger(name)


logger.add_handler()

message = Message(logger.name)
message.debug('This is debug')
message.info('This is info')
message.warning('This is warning')
message.error('This is error')
message.critical('This is critical')

