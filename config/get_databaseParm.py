# -*- coding:utf-8 -*-
# @Time   : 2018-11-30 17:50
# @Author : YangWeiMin

import os
import yaml

cur_path = os.path.dirname(os.path.realpath(__file__))
parm_path = os.path.join(cur_path, 'database_parm.yaml')

def database_parm():
    """获取数据库参数"""
    with open(parm_path, 'r', encoding='utf-8') as f:
        parm_data = yaml.load(f)
        return parm_data
