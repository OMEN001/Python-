"""
============================
Author:柠檬班-木森
Time:2019/10/22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
# from HTMLTestRunnerNew import HTMLTestRunner

from py23_13day.login_test_case import TestLogin
# from py23_13day import test_login_case


"""
这个是测试程序启动文件

第一步：创建一个测试套件对象（unittest.TestSuite）

第二步：将测试用例 加入到测试套件中
    unittest.TestLoader():专门用来加载测试用例到套件

第三步：创建一个测试运行程序对象（unittest.TextTestRuner）

第四步：通过运行程序，期执行测试套件中的测试用例

"""



# 第一步 创建测试套件对象
suite = unittest.TestSuite()

# 第二步:将测试用例 加入到测试套件中

# # 第一种方法：将一条测试用例加入测试套件中
# # 创建测试用例对象：第一参数是测试用例的方法名（必须要传）
# case = TestLogin("test_login_pass")
# # 将测试用例对象，加入测试套件
# suite.addTest(case)
#
# case2 = TestLogin("test_login_pwd_6")
# # 将测试用例对象，加入测试套件
# suite.addTest(case2)

# 第二种方法：将测试用例类中所有的测试用例，加入到测试套件
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLogin))


# 第三种方法：将一个模块中的所有测试用例 加载到测试套件
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login_case))

# 第四种方法：通过一个目录，去导入改目录下的所有模块种的测试用例
# loader = unittest.TestLoader()
# suite.addTest(loader.discover(r'C:\project\py23_class\py23_13day'))

# 第三步：创建一个测试运行程序对象
runner = unittest.TextTestRunner()

# runner = HTMLTestRunner(stream=open('report.html','wb'),
#                         title='python23期的第一份测试报告',
#                         description="辛辛苦苦学了一个月，终于生成了一份测试报告了",
#                         tester="musen")


# 第四步：通过运行程序，期执行测试套件中的测试用例
runner.run(suite)



