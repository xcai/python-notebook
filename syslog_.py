#coding: utf8
import syslog
import sys
import traceback

class Logger(object):
    
    facility = syslog.LOG_LOCAL6
    
    def __init__(self, id):
        self.id = id
        syslog.openlog(self.id, syslog.LOG_NDELAY, self.facility)
    
    def debug(self, msg):
        self.__log(syslog.LOG_DEBUG, msg)

    def info(self, msg):
        self.__log(syslog.LOG_INFO, msg)
    
    def notice(self, msg):
        self.__log(syslog.LOG_NOTICE, msg)
    
    def warn(self, msg):
        self.__log(syslog.LOG_WARNING, msg)
    
    def error(self, msg):
        self.__log(syslog.LOG_ERR, msg)
    
    def exception(self, ex):
        self.error(self.__exception_msg(ex))
    
    def __exception_msg(self, ex):
        t, v, tb = sys.exc_info()
        return '%s,%s,%s,%s' % (traceback.format_tb(tb), t, v, ex)
    
    def __log(self, cate, msg):
        if type(msg) == unicode:
            syslog.syslog(cate, msg.encode('utf8'))
        else:
            syslog.syslog(cate, msg)
        

class StdLogger():
    
    def __init__(self, id):
        self.id = id
    
    def debug(self, msg):
        self.__log('Debug', msg)

    def info(self, msg):
        self.__log('Info', msg)
    
    def notice(self, msg):
        self.__log('Notice', msg)
    
    def warn(self, msg):
        self.__log('Warning', msg)
    
    def error(self, msg):
        self.__log('Error', msg)
    
    def exception(self, ex):
        self.error(self.__exception_msg(ex))
    
    def __exception_msg(self, ex):
        t, v, tb = sys.exc_info()
        return '%s,%s,%s,%s' % (traceback.format_tb(tb), t, v, ex)
    
    def __log(self, cate, msg):
        if type(msg) == unicode:
            print '%s: %s|%s' % (cate, self.id, msg.encode('utf8'))
        else:
            print '%s: %s|%s' % (cate, self.id, msg)


logger = Logger('ProjectName')

