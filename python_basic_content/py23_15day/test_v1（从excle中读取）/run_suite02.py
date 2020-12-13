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
from read_excle02 import ReadExcle


# 创建测试套件
suite = unittest.TestSuite()



# 读取excle中的用例数据
read = ReadExcle('cases.xlsx','register')
cases= read.read_data_obj()
print(cases)
# 加载用例到套件
for case_data in cases:
    case = RegisterTestCase("test_register",case_data)
    suite.addTest(case)




# 生成html文件的的测试报告

with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)
