# -*- coding:utf-8 -*-
# @Time   : 2018-11-29 19:05
# @Author : YangWeiMin

import json
import requests
import unittest
from common.assert_equal import AssertEqual
from common.common_method import CommonMethod
from common.pgsql_connect import PgsqlUtil
from config.get_parm import GetParm


class Order(unittest.TestCase):
    local_day = CommonMethod().get_local_day()
    local_min = CommonMethod().get_local_min()
    p = PgsqlUtil()
    Api = GetParm().getApiParm()

    def test_01(self):
        """查询旺店订单"""
        data = json.dumps({
            'page_number': '1',
            'order_status': '0'
        })
        url = CommonMethod().geturl(data, 'queryStdomOrder')
        request = requests.post(url, data)
        AssertEqual().query_assert_equal(request, '旺店订单')


if __name__ == '__main__':
    unittest.main()
