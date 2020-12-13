import unittest
from selenium import webdriver
import time

from web_20191228.PageObjects.login_page import LoginPage
from web_20191228.PageObjects.home_page import HomePage

from web_20191228.TestDatas import Common_Datas as CD
from web_20191228.TestDatas import login_datas as LD

import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问 系统登陆页面
        self.driver.get(CD.login_url)
        self.lp = LoginPage(self.driver)

    def tearDown(self) -> None:
        # 退当前会话
        self.driver.quit()


    def test_login_0_success(self):
        # 步骤
        # 1、登陆页面 - 登陆操作
        self.lp.login(LD.success_data["username"],LD.success_data["passwd"])
        # 断言
        time.sleep(2)
        self.assertEqual(LD.success_data["check_url"],self.driver.current_url)
        # 2、首页 - 确认 我的帐号 元素是否存在。
        self.assertTrue(HomePage(self.driver).user_is_existed())



    @ddt.data(*LD.wrong_datas)
    def test_login_1_failed_by_wrong_datas(self,case):
        # 步骤
        # 1、登陆页面 - 登陆操作
        self.lp.login(case["username"],case["passwd"])
        # 断言
        self.assertEqual(self.lp.get_error_msg_from_login_form(),case["check"])
