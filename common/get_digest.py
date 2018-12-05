# -*- coding:utf-8 -*-
# @Time   : 2018-11-06 16:12
# @Author : YangWeiMin

import hashlib
from common.get_timestamp import time_stamp
from config.get_tenantParm import tenant_Parm


def diggest_data(request_data, timestamp):
    """数据签名公共方法"""
    appkey = tenant_Parm()['appkey']
    key = request_data + '|' + appkey + '|' + timestamp
    digest = hashlib.md5(key.encode('UTF-8')).hexdigest()
    return digest




