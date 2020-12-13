"""
============================
Author:柠檬班-木森
Time:2019/10/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
import test_cases
from HTMLTestRunnerNew import HTMLTestRunner

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_cases))




with open('zy_report.html', 'wb') as fb:
    # 创建测试运行程序
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')
    # 执行测试套件中的用例
    runner.run(suite)



