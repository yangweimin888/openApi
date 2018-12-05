# -*- coding:utf-8 -*-
# @Time   : 2018-11-29 19:39
# @Author : YangWeiMin

import logging
import time
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path),'logs')

if not os.path.exists(log_path):os.mkdir(log_path)

class Log(object):
    """编写日志公共方法"""

    def console(self,level,message):
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志的输出格式
        self.formatter = logging.Formatter('%(asctime)s %(filename)s [%(lineno)d] %(levelname)s %(message)s')
        # 创建一个FileHandler，将日志写在本地
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler将日志输入到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志重复输出
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)