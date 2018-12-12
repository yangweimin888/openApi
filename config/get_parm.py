# -*- coding:utf-8 -*-
# @Time   : 2018-12-10 19:02
# @Author : YangWeiMin
import os
import yaml


class GetParm(object):


    def openParmFile(self, path):
        """公共方法，读取参数文件"""
        self.parm_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
        with open(self.parm_path, 'r', encoding='utf-8') as f:
            data = yaml.load(f)
            return data


    def getApiParm(self):
        """获取接口数据"""
        api = self.openParmFile('api_parm.yaml')
        return api

    def getDataBaseparm(self):
        """获取数据库参数"""
        database_parm = self.openParmFile('database_parm.yaml')
        return database_parm


    def getTenantParm(self):
        """获取企业参数"""
        tenant_parm = self.openParmFile('tenant_parm.yaml')
        return tenant_parm

