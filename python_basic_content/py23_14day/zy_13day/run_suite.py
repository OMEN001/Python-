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
import testcases

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件


# 方式一：添加一个测试用例类中的所有用例
# loader：用例往测试套件中加载测试用例的
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))

# 方式二：添加一个模块中所有的测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(testcases))



# 生成html文件的的测试报告

with open('zy_report.html', 'wb') as fb:
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们21期的第一份报告作业',
                            tester='MuSen')

    runner.run(suite)


