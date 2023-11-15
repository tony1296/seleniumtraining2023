import logging
import loggingconcepts.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.info("***method1logs***")
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method3(self):

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()
