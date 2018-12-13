# -*- coding:utf-8 -*-
# @Time   : 2018-12-12 17:36
# @Author : YangWeiMin

import json
import requests
import unittest
from common.assert_equal import AssertEqual
from common.common_method import CommonMethod
from common.pgsql_connect import PgsqlUtil
from config.get_parm import GetParm


class Esss(unittest.TestCase):
    """进销存接口测试用例"""
    local_day = CommonMethod().get_local_day()
    local_min = CommonMethod().get_local_min()
    p = PgsqlUtil()
    Api = GetParm().getApiParm()


    # def test_01(self):
    #     """新增兑换货物"""
    #     data = json.dumps({
    #         'cm_code': self.p.get_CmCode('小杨专用经销商'),
    #         'business_name': '兑换货物',
    #         'creator_id': self.p.get_creator_id('小杨'),
    #         'car_code': self.p.get_car_code('A10086'),
    #         'num': 2,
    #         'prod_code': self.p.get_pd_code('ck002'),
    #         'unit_name': self.p.get_unit_name('ck002')
    #     })
    #     url = CommonMethod().geturl(data, 'addEsssExChangeProduct')
    #     request = requests.post(url, data)
    #     AssertEqual().add_assert_equal(request, '兑换货物', self.p.get_car_exchangeId())
    #
    #
    # def test_02(self):
    #     """审批兑换货物"""
    #     data = json.dumps({
    #         'id': self.p.get_car_exchangeId(),
    #         'verifyType': '1',
    #         'confirm_emp_code': self.p.get_emp_code('yang')
    #     })
    #     url = CommonMethod().geturl(data, 'verifyEsssExChangeProduct')
    #     request = requests.post(url, data)
    #     AssertEqual().verify_assert_equal(request, '兑换货物')
    #
    #
    # def test_03(self):
    #     """查询兑换货物"""
    #     data = json.dumps({
    #         'page_number': '1',
    #         'page_length': 10
    #     })
    #     url = CommonMethod().geturl(data, 'queryEsssExChangeProduct')
    #     request = requests.post(url, data)
    #     AssertEqual().query_assert_equal(request, '兑换货物')
    #
    #
    # def test_04(self):
    #     """新增调拨单"""
    #     data = json.dumps({
    #         'date': self.local_day,
    #         'creator_id': self.p.get_creator_id('小杨'),
    #         'emp_code': self.p.get_emp_code('yang'),
    #         'from_storehouse_code': self.p.from_storehouse_code('小杨专用仓库'),
    #         'to_storehouse_code': self.p.to_storehouse_code('小王专用仓库'),
    #         'products': [{
    #             'enable_num': 2,
    #             'input_unit': self.p.get_input_unit('ck002'),
    #             'prod_id': self.p.get_pd_id('ck002'),
    #             'prod_code': self.p.get_pd_code('ck002')
    #         }]
    #     })
    #     url = CommonMethod().geturl(data, 'addEsssStoreHouseChange')
    #     request = requests.post(url, data)
    #     AssertEqual().add_assert_equal(request, '调拨单', self.p.get_storehouse_changeId())
    #
    #
    # def test_05(self):
    #     """审批调拨单"""
    #     data = json.dumps({
    #         'id': self.p.get_storehouse_changeId(),
    #         'approvalType': '2',
    #         'confirm_emp_code': self.p.get_emp_code('yang')
    #     })
    #     url = CommonMethod().geturl(data, 'verifyEsssStoreHouseChange')
    #     request = requests.post(url, data)
    #     AssertEqual().verify_assert_equal(request, '调拨单')
    #
    #
    # def test_06(self):
    #     """查询调拨单"""
    #     data = json.dumps({
    #         'page_number': '1',
    #         'status': '1',
    #         'code': self.p.get_storehouse_changeCode()
    #     })
    #     url = CommonMethod().geturl(data, 'queryEsssStoreHouseChange')
    #     request = requests.post(url, data)
    #     AssertEqual().query_assert_equal(request, '调拨单')


    # def test_07(self):
    #     """新增库存盘点单"""
    #     data = json.dumps({
    #         'emp_code': self.p.get_emp_code('yang'),
    #         'inventory_status': '1',
    #         'inventory_type': '2',
    #         'date': self.local_day,
    #         'storehouse_code': self.p.from_storehouse_code('小杨专用仓库'),
    #         'remarks': '123',
    #         'prods': [{
    #             'prod_code': self.p.get_pd_code('ck002'),
    #             'actual_stock': '500',
    #             'sequ': '1'
    #         }]
    #     })
    #     url = CommonMethod().geturl(data, 'addEsssInventory')
    #     request = requests.post(url, data)
    #     AssertEqual().add_assert_equal(request, '库存盘点单', self.p.get_inventoryId())
    #
    #
    # def test_08(self):
    #     """审核库存盘点单"""
    #     data = json.dumps({
    #         'id': self.p.get_inventoryId()
    #     })
    #     url = CommonMethod().geturl(data, 'verifyEsssInventory')
    #     request = requests.post(url, data)
    #     AssertEqual().verify_assert_equal(request, '库存盘点单')


    def test_09(self):
        """新增车辆盘点单"""
        data = json.dumps({
            'emp_name': self.p.get_emp_name('yang'),
            'emp_code': self.p.get_emp_code('yang'),
            'inventory_status': '0',
            'inventory_type': '2',
            'date': self.local_day,
            'car_code': self.p.get_car_code('A10086'),
            'remarks': '123',
            'prods': [{
                'prod_code': self.p.get_pd_code('ck002'),
                'actual_stock': '20',
                'difference_stock': '20'
            }]
        })
        url = CommonMethod().geturl(data, 'addEsssCarInventory')
        request = requests.post(url, data)
        AssertEqual().add_assert_equal(request, '车辆盘点单', self.p.get_car_InventoryId())


    def test_10(self):
        """审核车辆盘点单"""
        data = json.dumps({
            'id': self.p.get_car_InventoryId()
        })
        url = CommonMethod().geturl(data, 'verifyEsssCarInventory')
        request = requests.post(url, data)
        AssertEqual().verify_assert_equal(request, '车辆盘点单')


if __name__ == '__main__':
    unittest.main()
