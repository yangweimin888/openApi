# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 15:26
# @Author : YangWeiMin
import psycopg2
from config.get_databaseParm import database_parm


class PgsqlUtil(object):

    def __init__(self):
        parm = database_parm()
        self.host = parm['host']
        self.port = parm['port']
        self.user = parm['user']
        self.password = parm['password']
        self.database = parm['database']
        # 连接数据库
        try:
            self.conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        except Exception as e:
            print('数据库连接异常：%s'%e)

    def pgsql_execute(self,sql):
        '''执行sql语句'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            # sql执行异常后回滚
            self.conn.rollback()
            print('执行SQL语句出现异常：%s' %e)
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

    def pgsql_getString(self,sql):
        '''查询某个字段的对应值'''
        rows = self.pgsql_execute(sql)
        if rows != None:
            for row in rows:
                for i in row:
                    return i


    def get_esssCarSaleBasId(self):
        '''获取车销单最新id'''
        sql = " SELECT id FROM esss_car_sale_bas ORDER BY create_time DESC LIMIT 1;"
        esss_id = self.pgsql_getString(sql)
        return esss_id

    def get_stdOrderSent(self):
        '''获取发货单id'''
        sql = "SELECT id from std_order_sent ORDER BY create_time DESC LIMIT 1;"
        sent_id = self.pgsql_getString(sql)
        return sent_id

    def get_CmId(self):
        '''获取客户id'''
        sql = "SELECT id FROM bas_cm_customer WHERE name = '小杨专用经销商';"
        cm_id = self.pgsql_getString(sql)
        return cm_id

    def get_CmCode(self):
        '''获取客户code'''
        sql = "SELECT code FROM bas_cm_customer WHERE name = '小杨专用经销商';"
        cm_code = self.pgsql_getString(sql)
        return cm_code

    def get_storehouse_changeId(self):
        '''获取调拨单id'''
        sql = "SELECT id FROM esss_storehouse_change_bas ORDER BY create_time DESC LIMIT 1;"
        storehouse_changeId = self.pgsql_getString(sql)
        return storehouse_changeId

    def get_inventoryId(self):
        '''获取库存盘点单id'''
        sql = "SELECT id FROM esss_inventory_bas ORDER BY create_time DESC LIMIT 1;"
        inventory_id = self.pgsql_getString(sql)
        return inventory_id

    def get_car_exchangeId(self):
        '''获取兑换货物单据id'''
        sql = "SELECT id FROM esss_car_exchange_product_bas ORDER BY create_time DESC LIMIT 1;"
        car_exchangeId = self.pgsql_getString(sql)
        return car_exchangeId

    def get_car_InventoryId(self):
        '''获取车辆盘点单id'''
        sql = "SELECT id FROM esss_car_inventory_bas ORDER BY create_time DESC LIMIT 1;"
        car_InventoryId = self.pgsql_getString(sql)
        return car_InventoryId

    def get_InOtherOrderId(self):
        '''获取其他入库单id'''
        sql = "SELECT id FROM esss_storehouse_in_bas ORDER BY create_time DESC LIMIT 1;"
        InOtherOrderId = self.pgsql_getString(sql)
        return InOtherOrderId


    def get_OutOtherOrderId(self):
        '''获取其他出库单id'''
        sql = "SELECT id FROM esss_storehouse_out_bas ORDER BY create_time DESC LIMIT 1;"
        OutOtherOrderId = self.pgsql_getString(sql)
        return OutOtherOrderId