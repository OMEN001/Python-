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
from mylogger import log,MyLogger


# 不要重复去创建日志收集器，创建对各收集器，日志会重复收集
# log2 = MyLogger.create_logger()
# log3 = MyLogger.create_logger()

# 创建测试套件
suite = unittest.TestSuite()

log.info("测试套件创建成功")

# 加载用例用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_cases))

log.info("测试套件加载完毕")


with open('zy_report.html', 'wb') as fb:
    # 创建测试运行程序
    runner = HTMLTestRunner(stream=fb,
                            title='柠檬班测试报告',
                            description='这是我们23期的第一份报告作业',
                            tester='MuSen')
    # 执行测试套件中的用例
    runner.run(suite)

log.info("所有的用例已经执行完毕")



