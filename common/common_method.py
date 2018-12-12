# -*- coding:utf-8 -*-
# @Time   : 2018-12-10 19:50
# @Author : YangWeiMin
import hashlib
from config.get_parm import GetParm
import time
import json


class CommonMethod(GetParm):
    """程序中用到的公共方法"""
    Api = GetParm().getApiParm()


    def diggest_data(self, request_data, timestamp):
        """
        数据签名加密
        :param request_data: 接口中的请求体
        :param timestamp: 时间戳
        :return: 返回一个加密后的对象
        """
        appkey = self.getTenantParm()['appkey']
        key = request_data + '|' + appkey + '|' + timestamp
        digest = hashlib.md5(key.encode('UTF-8')).hexdigest()
        return digest

    @staticmethod
    def time_stamp():
        """
        获取当前时间戳
        :return: 时间戳对象
        """
        timestamp = time.strftime('%Y%m%d%H%M%S')
        return timestamp

    @staticmethod
    def get_local_day():
        """格式化时间,精确到天"""
        local_day = time.strftime('%Y-%m-%d')
        return local_day

    @staticmethod
    def get_local_sec():
        """格式化时间,精确到秒"""
        local_sec = time.strftime('%Y-%m-%d %X')
        return local_sec

    @staticmethod
    def get_local_min():
        """格式化时间，精确到分钟"""
        local_min = time.strftime('%Y-%m-%d %H:%m')
        return local_min


    # def request_data(self, **kwargs):
    #     """将字典格式的请求参数转换成json格式"""
    #     for key, value in kwargs.items():
    #         data = json.dumps({
    #             key: value
    #         })
    #         return data


    def geturl(self, request_data, api_name):
        """拼接url地址"""
        host = self.getTenantParm()['host']
        timestamp = self.time_stamp()
        open_id = self.getTenantParm()['open_id']
        msg_id = GetParm().getTenantParm()['msg_id']
        api = self.Api[api_name]
        digest = self.diggest_data(request_data, timestamp)
        url = 'http://' + host + api + str(open_id) + '/' + str(timestamp) + '/' + digest + '/' + msg_id
        return url



