# -*- coding:utf-8 -*-
# @Time   : 2018-11-28 10:13
# @Author : YangWeiMin

import yaml
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
parm_path = os.path.join(cur_path, 'tenant_parm.yaml')

def tenant_Parm():
    """获取企业参数的公共方法"""
    with open(parm_path, 'r', encoding='utf-8') as f:
        parm_data = yaml.load(f)
        return parm_data


