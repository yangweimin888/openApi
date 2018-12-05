# -*- coding:utf-8 -*-
# @Time   : 2018-11-28 15:08
# @Author : YangWeiMin
# -*- coding:utf-8 -*-

import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os



"""
执行用例并发送报告，分四个步骤:
第一步：加载用例
第二步：执行用例
第三步：获取最新的测试报告
第四步：发送邮件
"""


#当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="case",rule="test*.py"):
    """
    作用：第一步，加载所有测试用例
    :param caseName:
    :param rule:
    :return:
    """
    case_path = os.path.join(cur_path,caseName) #用例文件夹
    #如果不存在这个文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print (discover)
    return discover


def run_case(all_case,reportName="report"):
    """
    作用：第二步，执行所有的用例，并把执行结果写入HTML测试报告中
    :param all_case:
    :param reportName:
    :return:
    """
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    #如果不存在report文件夹，则自动创建
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now+"result.html")
    fp = open(report_abspath,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="openApi接口自动化测试报告:",description="用例执行情况：")

    #调用add_case函数返回值
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    """
    作用：获取最新的测试报告
    :param report_path:
    :return:
    """
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print ("最新的测试报告：" + lists[-1])
    #找到最新生成的测试报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file

def send_mail(subject,sender,psw,receiver,smtpserver,report_file,port):
    """
    作用：将最新的测试报告通过邮件进行发送
    :param sender:发件人
    :param psw:QQ邮箱授权码
    :param receiver:收件人
    :param smtpserver:QQ邮箱服务
    :param report_file:
    :param port:端口
    :return:
    """
    with open(report_file,"rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype="html",_charset="utf-8")
    msg["Subject"] = subject
    msg["from"] = sender
    msg["to"] = ','.join(receiver)
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp =smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    # 用户名和密码
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print ("测试报告邮件已发送成功 !")


if __name__ == '__main__':
    all_case = add_case()# 1、加载用例
    run_case(all_case)# 2、执行用例
    # 获取最新的测试报告
    report_path = os.path.join(cur_path,"report") # 用例文件夹
    report_file = get_report_file(report_path) # 3、获取最新的测试报告
    # 邮箱配置
    from config import readConfig
    subject = readConfig.subject
    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    send_mail(subject,sender, psw, receiver, smtp_server, report_file, port) # 4、最后一步发送报告



