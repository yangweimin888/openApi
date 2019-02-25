# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 15:26
# @Author : YangWeiMin
import psycopg2
from config.get_parm import GetParm

class PgsqlUtil(GetParm):

    def __init__(self):
        parm = self.getDataBaseparm()
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


    def get_CmId(self ,code):
        '''获取客户id'''
        sql = "SELECT id FROM bas_cm_customer WHERE code = '%s';" % code
        cm_id = self.pgsql_getString(sql)
        return cm_id


    def get_CmCode(self, name):
        '''获取客户code'''
        sql = "SELECT code FROM bas_cm_customer WHERE name = '%s';" % name
        cm_code = self.pgsql_getString(sql)
        return cm_code


    def get_storehouse_changeId(self):
        '''获取调拨单id'''
        sql = "SELECT id FROM esss_storehouse_change_bas ORDER BY create_time DESC LIMIT 1;"
        storehouse_changeId = self.pgsql_getString(sql)
        return storehouse_changeId


    def get_storehouse_changeCode(self):
        """获取调拨单单号"""
        sql = "SELECT code  FROM esss_storehouse_change_bas ORDER BY create_time DESC LIMIT 1;"
        storehouse_changeCode = self.pgsql_getString(sql)
        return storehouse_changeCode


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


    def get_creator_id(self, name):
        """获取创建人id"""
        sql = "SELECT id FROM sm_user WHERE name = '%s';" % name
        creator_id = self.pgsql_getString(sql)
        return creator_id


    def get_emp_code(self, code):
        """获取业务员编码"""
        sql = "SELECT code FROM sm_user WHERE code = '%s';" % code
        emp_code = self.pgsql_getString(sql)
        return emp_code


    def get_emp_name(self, code):
        """获取员工姓名"""
        sql = "select name from sm_user where code = '%s'" %code;
        emp_name = self.pgsql_getString(sql)
        return emp_name


    def from_storehouse_code(self, name):
        """获取转出仓库code"""
        sql = "SELECT code FROM esss_storehouse WHERE name = '%s';" % name
        storehouse_code = self.pgsql_getString(sql)
        return storehouse_code


    def to_storehouse_code(self, name):
        """获取转入仓库code"""
        sql = "SELECT code FROM esss_storehouse WHERE name = '%s';" % name
        storehouse_code = self.pgsql_getString(sql)
        return storehouse_code


    def get_input_unit(self, code):
        """根据商品code获取商品的基本单位id"""
        sql = "select a.id from bas_pd_unit a JOIN bas_pd_product b ON a.pd_id = b.id WHERE b.code = '%s'" % code + " and is_base = '1';"
        input_unit = self.pgsql_getString(sql)
        return input_unit


    def get_pd_id(self, code):
        """根据商品code获取商品id"""
        sql = "SELECT id FROM bas_pd_product WHERE code = '%s';" %code
        pd_id = self.pgsql_getString(sql)
        return pd_id


    def get_pd_code(self, code):
        """获取商品code"""
        sql = "SELECT code FROM bas_pd_product WHERE code = '%s';" %code
        pd_code = self.pgsql_getString(sql)
        return pd_code


    def get_unit_name(self, code):
        """获取单位名称"""
        sql = "SELECT b.unit_name FROM bas_pd_product a JOIN bas_pd_unit b ON a.id = b.pd_id WHERE a.code = '%s'" %code + " and b.is_base = '1';"
        pd_name = self.pgsql_getString(sql)
        return pd_name


    def get_car_code(self, name):
        """获取车辆code"""
        sql = "SELECT code FROM esss_storehouse WHERE name = '%s';" % name
        car_code = self.pgsql_getString(sql)
        return car_code


    def get_account(self, name):
        """获取账户信息"""
        sql = "select name from esss_account where name = '%s';" % name
        account_name = self.pgsql_getString(sql)
        return account_name


    def get_esss_receive_id(self):
        sql = "SELECT id FROM esss_receivable_history_bas ORDER BY create_time DESC LIMIT 1;"
        receive_id = self.pgsql_getString(sql)
        return receive_id