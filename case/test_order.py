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
        request = requests.post(url,data)
        AssertEqual().query_assert_equal(request, '旺店订单')


    def test_02(self):
        """新增调拨单"""
        data = json.dumps({
            'date': self.local_day,
            'creator_id': self.p.get_creator_id(),
            'emp_code': self.p.get_emp_code(),
            'from_storehouse_code': self.p.from_storehouse_code(),
            'to_storehouse_code': self.p.to_storehouse_code(),
            'products': [{
                'enable_num': 2,
                'input_unit': self.p.get_input_unit('ck002'),
                'prod_id': self.p.get_pd_id('ck002'),
                'prod_code': self.p.get_pd_code('ck002')
            }]
        })
        url = CommonMethod().geturl(data, 'addEsssStoreHouseChange')
        request = requests.post(url, data)
        AssertEqual().add_assert_equal(request, '调拨单', self.p.get_storehouse_changeId())




if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()