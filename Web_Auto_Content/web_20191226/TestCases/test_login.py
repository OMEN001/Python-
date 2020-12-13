import unittest
from selenium import webdriver
import time

from web_20191226.PageObjects.login_page import LoginPage
from web_20191226.PageObjects.home_page import HomePage

import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问 系统登陆页面
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        # 退当前会话
        self.driver.quit()


    def test_login_success(self):
        # 步骤
        # 1、登陆页面 - 登陆操作
        self.lp.login("18684720553","python")
        # 断言
        # 1、url发生改变: http://120.78.128.25:8765/Index/index
        time.sleep(2)
        self.assertEqual("http://120.78.128.25:8765/Index/index",self.driver.current_url)
        # 2、首页 - 确认 我的帐号 元素是否存在。
        self.assertTrue(HomePage(self.driver).user_is_existed())


    wrong_datas = [
        {"username":"","passwd":"python","check":"请输入手机号"},
        {"username": "18684720553", "passwd": "", "check": "请输入密码"},
        {"username": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
    ]

    @ddt.data(*wrong_datas)
    def test_login_failed_by_wrong_datas(self,case):
        # 步骤
        # 1、登陆页面 - 登陆操作
        self.lp.login(case["username"],case["passwd"])
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_login_form(),case["check"])
