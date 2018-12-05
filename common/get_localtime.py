# -*- coding:utf-8 -*-
# @Time   : 2018-11-29 15:00
# @Author : YangWeiMin

import time

def get_local_day():
    '''格式化时间,精确到天'''
    local_day = time.strftime('%Y-%m-%d')
    return local_day


def get_local_sec():
    '''格式化时间,精确到秒'''
    local_sec = time.strftime('%Y-%m-%d %X')
    return local_sec


def get_local_min():
    '''格式化时间，精确到分钟'''
    local_min = time.strftime('%Y-%m-%d %H:%m')
    return local_min


