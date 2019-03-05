# -*- coding:utf-8 -*-
# '''
# Created on 2018-6-11
# @author: Joy
# '''
# import os
# import sys
# import logging.handlers
# from urllib3.connectionpool import xrange
#
# """各种日志级别对应的值
# CRITICAL = 50
# ERROR = 40
# WARNING = 30
# INFO = 20
# DEBUG = 10
# NOTSET = 0
# """
# _logger_level = 30
# _dictLogger = {}
# _default_log_name = "common_api.log"
# __doc__ = """"""
# class LogManage:
#
#     def __init__(self,strFileName=_default_log_name,
#                  debug=_logger_level,
#                  bShowStreamLog = False,
#                  strSaveLogPath = None):
#
#         self.__logger = None
#         # 保存日志的文件名
#         self.__strFileName = strFileName
#         # 保存日志的文件路径
#         self.__strSaveLogPath = strSaveLogPath
#         # 单个文件大小设置为20M
#         self.__nLogFileSize = 20*1024*1024
#         # 最多保存10个文件
#         self.__nLogFileNum = 10
#         # 日志级别
#         self.__nLogLevel = debug
#         # 是否显示流日志
#         self.__bShowStreamLog = bShowStreamLog
#         # 日志格式
#         self.__objLogFormat = "[%(asctime)s][%(filename)s][%(lineno)s][thread:%"
#         self.__objLogFormat += "(thread)s][process:%(process)s][%(levelname)s] %(message)s"
#
#         self.__initLogger()
#
#     def __initLogger(self):
#         # 同一个logger只允许初始化一次
#         global _dictLogger
#         logger = _dictLogger.get(self.__strFileName,None)
#         if logger != None:
#             self.__logger = logger
#             return
#
#         # 保存的文件夹不存在，则创建
#         dirFileName = os.path.dirname(self.__strFileName)
#         strFileName = os.path.basename(self.__strFileName)
#
#         if  dirFileName == "" or dirFileName == ".":
#             dirFileName = sys.path[0]
#             dirFileName = os.path.join(dirFileName,"logs")
#         if self.__strSaveLogPath:
#             dirFileName = os.path.join(self.__strSaveLogPath,"logs")
#         dirFileName = os.path.realpath(dirFileName)
#         if not os.path.exists(dirFileName):
#             os.makedirs(dirFileName)
#         self.__strFileName = os.path.join(dirFileName,strFileName)
#         # 文件handler
#         fileHandler = logging.handlers.RotatingFileHandler(self.__strFileName,
#                                             maxBytes = self.__nLogFileSize,
#                                             backupCount = self.__nLogFileNum)
#         # 实例化formatter
#         formatter = logging.Formatter(self.__objLogFormat)
#         fileHandler.setFormatter(formatter)
#         self.__logger = logging.getLogger(self.__strFileName)
#         # 为logger添加handler
#         self.__logger.addHandler(fileHandler)
#         _dictLogger[self.__strFileName] = self.__logger
#         # 增加一个流handler
#         steamHandler = logging.StreamHandler()
#         steamHandler.setFormatter(formatter)
#         self.steamHandler = steamHandler
#         if self.__bShowStreamLog:
#             self.__logger.addHandler(steamHandler)
#
#         #设置日志级别
#         self.__logger.setLevel(self.__nLogLevel)
#
#     def addStreamHandler(self):
#         # 增加一个流handler
#         try:
#             # 如果已经增加直接返回
#             if self.__strShowStreamLog:
#                 return
#             self.__logger.addHandler(self.steamHandler)
#             self.__strShowStreamLog = True
#         except:
#             pass
#     def setLogLevel(self,logLevel):
#         # 重新设置日志级别
#         self.__logger.setLevel(self.__nLogLevel)
#
#     def getLogger(self):
#         return self.__logger
# def get_logger(strFileName=_default_log_name,
#                debug=_logger_level,
#                showStreamLog = False,
#                saveLogPath = None):
#
#     global _dictLogger
#     logger = _dictLogger.get(strFileName,None)
#     if logger != None:
#         return logger
#     objLogger = LogManage(strFileName,debug,showStreamLog,saveLogPath)
#     logger = objLogger.getLogger()
#
#     return logger
#
# def _testLog():
#
#     logger = get_logger(strFileName="D:\\python27File\\crmAutoTest\\testCase\\crm_login_test.py",
#                         debug=30,
#                         showStreamLog=True,
#                         saveLogPath=None)
#     logger.error("ERROR-ERROE-"*5)
#     logger.debug("DEBUG-DEBUG-"*5)
#     objLogger = LogManage("nameas.log")
#     logger = objLogger.getLogger()
#     for item in xrange(1):
#         logger.error("%5d"%item*50)
#     @classmethod
#     def info(cls, msg):
#      cls.log.info(msg)
#      return
#
#     @classmethod
#     def warning(cls, msg):
#       cls.log.warning(msg)
#       return
#
#     @classmethod
#     def error(cls, msg):
#       cls.log.error(msg)
#       return
# if __name__ == "__main__":
#     _testLog()
# from xml import etree
# import logging.handlers
# import logging
# import os
# import sys
#
# # 提供日志功能
# class logger:
#   # 先读取XML文件中的配置数据
#   # 由于config.xml放置在与当前文件相同的目录下，因此通过 __file__ 来获取XML文件的目录，然后再拼接成绝对路径
#   # 这里利用了lxml库来解析XML
#   root =etree.parse(os.path.join(os.path.dirname(__file__), 'config.xml')).getroot()
#   # 读取日志文件保存路径
#   logpath = root.find('logpath').text
#   # 读取日志文件容量，转换为字节
#   logsize = 1024*1024*int(root.find('logsize').text)
#   # 读取日志文件保存个数
#   lognum = int(root.find('lognum').text)
#   # 日志文件名：由用例脚本的名称，结合日志保存路径，得到日志文件的绝对路径
#   logname = os.path.join(logpath, sys.argv[0].split('/')[-1].split('.')[0])
#   # 初始化logger
#   log = logging.getLogger()
#   # 日志格式，可以根据需要设置
#   fmt = logging.Formatter('[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
#
#   # 日志输出到文件，这里用到了上面获取的日志名称，大小，保存个数
#   handle1 = logging.handlers.RotatingFileHandler(logname, maxBytes=logsize, backupCount=lognum)
#   handle1.setFormatter(fmt)
#   # 同时输出到屏幕，便于实施观察
#   handle2 = logging.StreamHandler(stream=sys.stdout)
#   handle2.setFormatter(fmt)
#   log.addHandler(handle1)
#   log.addHandler(handle2)
#
#   # 设置日志基本，这里设置为INFO，表示只有INFO级别及以上的会打印
#   log.setLevel(logging.INFO)

  # 日志接口，用户只需调用这里的接口即可，这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口

import  logging
import  os
import time
# log_path = r'D:\\python27File\\newcrmtest\\result\\test.log'
class loginmanger():
 # def __init__(self):
 #        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
 def consel_out(self ):
   logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='D:\\python27File\\newcrmtest\\result\\test.log',
                    filemode='w',
                    # encoding='utf-8'
                       )
#    logger = logging.getLogger()
#    logger.setLevel(logging.DEBUG)
#         # 创建一个handler，用于写入日志文件
#    fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
#    fh.setLevel(logging.DEBUG)
#         # 再创建一个handler，用于输出到控制台
#    ch = logging.StreamHandler()
#    ch.setLevel(logging.DEBUG)
#         # 定义handler的输出格式
#    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#    fh.setFormatter(formatter)
#    ch.setFormatter(formatter)
#         # 给logger添加handler
#    logger.addHandler(fh)
#    logger.addHandler(ch)
#         # 记录一条日志
#    if level == 'info':
#      logger.info(message)
#    elif level == 'debug':
#             logger.debug(message)
#    elif level == 'warning':
#             logger.warning(message)
#    elif level == 'error':
#             logger.error(message)
#    logger.removeHandler(ch)
#    logger.removeHandler(fh)
#         # 关闭打开的文件
#    fh.close()
#
# def debug(self,message):
#         self.consel_out('debug', message)
#
# def info(self,message):
#         self.consel_out('info', message)
#
# def warning(self,message):
#         self.consel_out('warning', message)
#
# def error(self,message):
#         self.consel_out('error', message)
   console = logging.StreamHandler()  # 定义console handler
   console.setLevel(logging.INFO)  # 定义该handler级别
   formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
   console.setFormatter(formatter)
  # Create an instance
  # logging.getLogger().addHandler(console)
  # logging.debug('logging debug')
  # logging.warning('logging warning')
  # logging.error('logging.error')
  # logging.critical('logging.critical')
  # logging.debug('this is a message')
 def info(self, msg):
      self.consel_out().info(msg)
      return
 def warning(self, msg):
     self.consel_out().warning(msg)
     return
 def error(self, msg):
       self.consel_out().error(msg)
       return

