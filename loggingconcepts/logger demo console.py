import logging
import logging.config

class LoggerDemoConsole():

    def testLog(self):
        #create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.DEBUG)

        #create console handler and set level to info
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)

        #create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        #add formatter to console handler
        consoleHandler.setFormatter(formatter)
        #add console to logger
        logger.addHandler(consoleHandler)

        #logging messages

        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()