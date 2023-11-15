"""
Logger demo
"""
import logging
import logging.config

class LoggerDemoConf():

    def testlog(self):
        #create logger
        logging.config.fileConfig('logging.config')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        #logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConf()
demo.testlog()