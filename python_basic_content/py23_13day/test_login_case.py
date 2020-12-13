"""
============================
Author:柠檬班-木森
Time:2019/10/22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
# from login import login_check

from python_content.py23_13day.login import login_check

"""
unittest是python中的官方库

1、设计测试用例
                           入参                预期
   1  正常登录的用例   正确的账号和密码             {"code": 0, "msg": "登录成功"}
   2  密码长度低于6位  正确账号，密码长度低于6位     {"code": 1, "mgs": "密码长度在6-18位之间"}
   3 密码长度大于18位  正确账号，密码长度低于18位    {"code": 1, "mgs": "密码长度在6-18位之间"}
   4 账号正确，密码有误 正确的账号 错误密码          {"code": 1, "msg": "账号或密码不正确"}

unittest.TestCase(测试用例类)，所有的测试用例类，都是继承于unittest.TestCase

每一条测试用例，就是测试用例类中的一个方法（方法名必须要用test开头）


"""


class TestLogin(unittest.TestCase):
    """登录校验的测试用例类"""

    def test_login_pass(self):
        # 准备测试用例 要用到的数据
        # 入参
        data = ['python23',"lemonban"]
        # 预期结果
        excepted = {"code": 0, "msg": "登录成功"}

        #  第一步 调用功能函数，传入参数
        result = login_check(*data)

        #  第二步  比对预期结果，和实际结果是否一致
        self.assertEqual(excepted,result)

    def test_login_pwd_6(self):
        # 准备测试用例 要用到的数据
        # 入参
        data = ['python23', "12345"]
        # 预期结果
        excepted = {"code": 1, "mgs": "密码长度在6-18位之间"}

        #  第一步 调用功能函数，传入参数
        result = login_check(*data)

        #  第二步  比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def test_login_pwd_18(self):
        # 准备测试用例 要用到的数据
        # 入参
        data = ['python23', "1234561234567123456"]
        # 预期结果
        excepted = {"code": 1, "mgs": "密码长度在6-18位之间"}

        #  第一步 调用功能函数，传入参数
        result = login_check(*data)

        #  第二步  比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def test_login_pws_error(self):
        # 准备测试用例 要用到的数据
        # 入参
        data = ['python23', "lemonba"]
        # 预期结果
        excepted = {"code": 1, "msg": "账号或密码不正确"}

        #  第一步 调用功能函数，传入参数
        result = login_check(*data)

        #  第二步  比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def setUp(self):
        # 每一条测试用例执行之前，都会执行
        print('{}开始执行了'.format(self))

    def tearDown(self) :
        # 每一条测试用例执行之后，都会执行
        print('{}执行完了'.format(self))

    @classmethod
    def setUpClass(cls):
        # 执行这个测试用例类中的测试用例之前会执行
        print('{}这个测试用例类开始执行了'.format(cls))

    @classmethod
    def tearDownClass(cls) :
        # 这个测试用例类中的测试用例全部执行完，就会执行改方法
        print('{}这个测试用例类的所有测试用例都执行完了，会执行这个方法'.format(cls))





