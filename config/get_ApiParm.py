# -*- coding:utf-8 -*-
# @Time   : 2018-11-29 14:35
# @Author : YangWeiMin

import yaml
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
parm_path = os.path.join(cur_path, 'api_parm.yaml')

def ApiParm():
    """公共方法，获取接口数据"""
    with open(parm_path, 'r', encoding='utf-8') as f:
        parm_data = yaml.load(f)
        return parm_data




