# -*- coding:utf-8 -*-
# @Time   : 2018-11-29 19:05
# @Author : YangWeiMin

import json
import requests
import unittest
from common.logger import Log
from config.get_tenantParm import tenant_Parm
from config.get_ApiParm import ApiParm
from common.get_timestamp import time_stamp
from common.get_digest import diggest_data
from common.pgsql_connect import PgsqlUtil
from common.get_localtime import get_local_day, get_local_min


class Order(unittest.TestCase):
    log = Log()
    host = tenant_Parm()['host']
    open_id = tenant_Parm()['open_id']
    timestamp = time_stamp()
    msg_id = tenant_Parm()['msg_id']
    local_day = get_local_day()
    local_min = get_local_min()
    p = PgsqlUtil()
    Api = ApiParm()

    def test_01(self):
        """查询旺店订单"""
        data = json.dumps({
            'page_number': '1',
            'order_status': '0'
        })

        api = self.Api['queryStdomOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        # response = json.loads(request_data['response_data'])
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('旺店订单查询成功')
        except Exception as e:
            self.log.error('旺店订单查询失败:%s' % e)
            self.log.error(request_data['return_msg'])


    def test_02(self):
        """查询订单发货(旺店发货)的数据"""
        data = json.dumps({
            'page_number': '1',
            'status': '1'
        })

        api = self.Api['queryStdomSent']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('订单发货（旺店发货）数据查询成功')
        except Exception as e:
            self.log.error('订单发货（旺店发货）数据查询失败:%s' % e)
            self.log.error(request_data['return_msg'])



if __name__ == '__main__':
    unittest.main()