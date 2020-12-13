"""
============================
Author:柠檬班-木森
Time:2019/10/23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from test_cases import RegisterTestCase

# 创建测试套件
suite = unittest.TestSuite()

cases = [
    {'data': ('python1', '123456', '123456'), "excepted": {"code": 1, "msg": "注册成功"}},
    {'data': ('python1', '1234567', '123456'), "excepted": {"code": 0, "msg": "两次密码不一致"}},
    {'data': ('python18', '1234567', '123456'), "excepted": {"code": 0, "msg": "该账户已存在"}},
]

# 加载用例到套件

# case_data={'data': ('python1', '123456', '123456'), "excepted": {"code": 1, "msg": "注册成功"}}

for case_data in cases:
    #创建一个对象
    #这里将test_case中的__init__方法进行了重写，因为父类的__init__方法只能传入（方法名）这一个参数
    #将方法重写之后传入了case_dta这个参数
    case = RegisterTestCase("test_register",case_data)  #给套件里面加载用例
    suite.addTest(case)




# 生成html文件的的测试报告

with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)
