# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 16:39
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


class Esss(unittest.TestCase):
    log = Log()
    host = tenant_Parm()['host']
    open_id = tenant_Parm()['open_id']
    timestamp = time_stamp()
    msg_id = tenant_Parm()['msg_id']
    local_day = get_local_day()
    local_min = get_local_min()
    p = PgsqlUtil()
    Api = ApiParm()

    # @unittest.skip('跳过')
    def test_01(self):
        '''新增调拨单'''
        data = json.dumps({
            "date": "2018-11-15",
            "creator_id": "5615317598638557453",
            "emp_code": "yang",
            "from_storehouse": "5397700700106920680",
            "from_storehouse_code": "CK0003",
            "to_storehouse": "6371391915086892205",
            "to_storehouse_code": "CK0002",
            "products": [{
                "enable_num": 2,
                "input_unit": "5300799796772067734",
                "prod_id": "7969449436184248660",
                "prod_code": "ck123",
                "prod_name": "柠檬茶",
                "remark": "哈哈哈"
            }]
        })

        api = self.Api['addEsssStoreHouseChange']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        response = json.loads(request_data['response_data'])
        print(response)
        self.assertEqual(response['id'], str(self.p.get_storehouse_changeId()))
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('新增调拨单成功')
        except Exception as e:
            self.log.error('新增调拨单失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_02(self):
        '''审批调拨单'''
        data = json.dumps({
            "id": self.p.get_storehouse_changeId(),
            "approvalType": "1",
            "confirm_emp_id": "5615317598638557453",
            "confirm_emp_code": "yang",
            "confirm_emp_name": "小杨"
        })

        api = self.Api['verifyEsssStoreHouseChange']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('调拨单审批成功')
        except Exception as e:
            self.log.error('调拨单审批失败:%s' % e)
            self.log.error(request_data['return_msg'])

    # @unittest.skip('跳过')
    def test_03(self):
        '''查询调拨单'''
        data =json.dumps({
            'page_number': '1',
            'status': '1',
            'code': 'DB201811050001'
        })
        api = self.Api['queryEsssStoreHouseChange']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('获取调拨单记录成功')
        except Exception as e:
            self.log.error('获取调拨单记录失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_04(self):
        '''新增库存盘点单'''
        data = json.dumps({
            "emp_name": "5615317598638557453",
            "inventory_status": "1",
            "inventory_type": "2",
            "date": "2018-11-15",
            "storehouse_code": "002",
            "storehouse_name": "瘦子仓库",
            "remarks": "123",
            "prods": [{
                "prod_code": "ck002",
                "actual_stock": "200",
                "sequ": "0"
            }]
        })

        api = self.Api['addEsssInventory']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('新增库存盘点单成功')
        except Exception as e:
            self.log.error('新增库存盘点单失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_05(self):
        '''审核库存盘点单'''
        data = json.dumps({
            'id': self.p.get_inventoryId()
        })

        api = self.Api['verifyEsssInventory']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('审核库存盘点单成功')
        except Exception as e:
            self.log.error('审核库存盘点单失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_06(self):
        '''新增兑换货物'''
        data = json.dumps({
            "cm_id": "8925553636869044991",
            "cm_code": "CUS000003",
            "cm_name": "小王专用经销商",
            "creator_id": "5615317598638557453",
            "business_name": "1",
            "car_id": "6586337398919781503",
            "car_name": "A10086",
            "num": 2,
            "unit": "5300799796772067734",
            "prod_id": "7969449436184248660",
            "unit_name": "瓶",
            "prod_code": "ck123",
            "remark": "哈哈哈"
        })

        api = self.Api['addEsssExChangeProduct']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('新增兑付货物成功')
        except Exception as e:
            self.log.error('兑换货物单据新增失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_07(self):
        '''审批兑换货物数据'''
        data = json.dumps({
            "id": self.p.get_car_exchangeId(),
            "verifyType": "1",
            "confirm_emp_id": "5615317598638557453",
            "confirm_emp_code": "yang",
            "confirm_emp_name": "小杨"
        })

        api = self.Api['verifyEsssExChangeProduct']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('审批兑付货物成功')
        except Exception as e:
            self.log.error('兑换货物单据审批失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_08(self):
        '''查询兑换货物数据'''
        data = json.dumps({
            "page_number": 1,
            'status': '1',
            'cm_id': self.p.get_CmId()
        })

        api = self.Api['queryEsssExChangeProduct']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('兑换货物数据查询成功')
        except Exception as e:
            self.log.error('兑换货物单据查询失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_09(self):
        '''新增车辆盘点单'''
        data = json.dumps({
            "emp_name": "小杨",
            "emp_code": "yang",
            "inventory_status": "0",
            "inventory_type": "2",
            "date": self.local_day,
            "car_code": "CL10086",
            "remarks": "123",
            "prods": [{
                "prod_code": "ck003",
                "actual_stock": "20",
            }]
        })

        api = self.Api['addEsssCarInventory']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('车辆盘点单新增成功')
        except Exception as e:
            self.log.error('车辆盘点单失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_10(self):
        '''审核车辆盘点单'''
        data = json.dumps({
            'id': self.p.get_car_InventoryId()
        })
        api = self.Api['verifyEsssCarInventory']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('车辆盘点单审核成功')
        except Exception as e:
            self.log.error('车辆盘点单审核失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_11(self):
        '''查询其他入库单'''
        data = json.dumps({
            "page_number": 1,
            "status": "1"
        })

        api = self.Api['queryInOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他入库单查询成功')
        except Exception as e:
            self.log.error('其他入库单查询失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_12(self):
        '''新增其他入库单'''
        data = json.dumps({
            "emp_id": "5615317598638557453",
            "emp_code": "yang",
            "emp_name": "小杨",
            "storehouse_id": "5397700700106920680",
            "storehouse_code": "CK0003",
            "prod_num": "1",
            "total_amount": "30",
            "total_count": "10",
            "remark": "123",
            "date": self.local_min,
            "bill_type": "1",
            "prods": [{
                "product_id": "7969449436184248660",
                "product_code": "ck123",
                "actual_price": "3",
                "num": "10",
                "amount": "30",
                "input_unit": "5300799796772067734",
                "remark": "123"
            }]
        })

        api = self.Api['addInOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他入库单新增成功')
        except Exception as e:
            self.log.error('其他入库单新增失败:%s' % e)
            self.log.error(request_data['return_msg'])


    # @unittest.skip('跳过')
    def test_13(self):
        '''审批其他入库单'''
        data = json.dumps({
            'id': self.p.get_InOtherOrderId(),
            'approvalType': '0'
        })
        api = self.Api['verifyInOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他入库单审批成功')
        except Exception as e:
            self.log.error('其他入库单审批失败:%s' % e)
            self.log.error(request_data['return_msg'])


    def test_14(self):
        """查询其他出库单"""
        data = json.dumps({
            "page_number": 1,
            "status": "1"
        })

        api = self.Api['queryOutOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他出库单查询成功')
        except Exception as e:
            self.log.error('其他出库单查询失败:%s' % e)
            self.log.error(request_data['return_msg'])


    def test_15(self):
        """新增其他出库单"""
        data = json.dumps({
            "emp_id": "5615317598638557453",
            "emp_code": "yang",
            "emp_name": "小杨",
            "storehouse_id": "5397700700106920680",
            "storehouse_code": "CK0003",
            "prod_num": "1",
            "total_amount": "3",
            "total_count": "1",
            "remark": "123",
            "date": self.local_min,
            "bill_type": "1",
            "prods": [{
                "product_id": "7969449436184248660",
                "product_code": "ck123",
                "actual_price": "3",
                "num": "1",
                "amount": "31",
                "input_unit": "5300799796772067734",
                "remark": "123"
            }]
        })

        api = self.Api['addOutOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他出库单新增成功')
        except Exception as e:
            self.log.error('其他出库单新增失败:%s' % e)
            self.log.error(request_data['return_msg'])


    def test_16(self):
        """审批其他出库单"""
        data = json.dumps({
            'id': self.p.get_OutOtherOrderId(),
            'approvalType': '1'
        })
        api = self.Api['verifyOutOtherOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('其他出库单审批成功')
        except Exception as e:
            self.log.error('其他出库单审批失败:%s' % e)
            self.log.error(request_data['return_msg'])

    def test_17(self):
        """查询车销单数据"""
        data = json.dumps({
            'page_number': '1',
            'status': '1',
            'cm_code': self.p.get_CmCode()
        })

        api = self.Api['queryCarSaleOrder']
        digest = diggest_data(data, self.timestamp)
        url = 'http://' + self.host + api + str(self.open_id) + '/' + str(self.timestamp) + '/' + digest + '/' + self.msg_id
        request = requests.post(url=url, data=data)
        request_data = json.loads(request.text)
        try:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request_data['return_code'], '0')
            self.log.info('车销单数据查询成功')
        except Exception as e:
            self.log.error('车销单数据查询失败:%s' % e)
            self.log.error(request_data['return_msg'])


if __name__ == '__main__':
    unittest.main()