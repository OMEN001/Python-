#!/usr/bin/python3
"""
@File    : test_login.py
@Time    : 2019/11/29 21:53
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
from selenium import webdriver
import logging
from Common import logger

from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage

from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD
import pytest

@pytest.fixture   # 申明这是一个 夹测试函数的   前置和后置的fixture
def init_driver():   # 名字叫做：setup
    # 前置代码
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    lp = LoginPage(driver)
    yield driver,lp   # 返回driver和lp变量
    # 后置代码
    driver.quit()

# @pytest.fixture("class")
# def myClass():
#     logging.info("=====我是测试类级别的前置=====")
#     yield
#     logging.info("=====我是测试类级别的后置=====")

@pytest.fixture
def dd():
    logging.info("=====我是测试用例 == 私人级别 === 的前置=====")
    yield
    logging.info("=====我是测试用例 == 私人级别 === 的后置=====")


@pytest.mark.usefixtures("myModule")
def test_module():
    logging.info("========== test modulev ===============")


@pytest.mark.nmb
@pytest.mark.usefixtures("init_driver")    # 这个类下面，所有的测试函数，都使用这个前置后置。
@pytest.mark.usefixtures("myClass")
class TestLogin:

    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(CD.login_url)
    #     self.lp = LoginPage(self.driver)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()
    """
    myClass 前置
    init_driver 前置
    用例1
    init_driver 后置
    init_driver 前置
    用例2
    init_driver 后置
    init_driver 前置
    用例3
    init_driver 后置
    myClass 后置
    """

    # 正常场景 - 登陆成功。
    # @pytest.mark.usefixtures("init_driver")    # 执行init_driver这个fixture的前置代码。
    @pytest.mark.smoke
    @pytest.mark.usefixtures("dd")
    def test_login_success(self,init_driver):  # init_driver = (driver,lp)
        logging.info("******* 登陆功能 - 正常场景用例：登陆成功 *******")
        # 调用登陆页面的。登陆行为。
        init_driver[1].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 - 首页当中，应该存在 退出元素。
        assert HomePage(init_driver[0]).check_user_exist() is True
        # 断言2 - url地址  应当为 http://120.78.128.25:8765/Index/index
        assert init_driver[0].current_url == LD.success_data["check_url"]

    def demo(self):
        pass

        # 异常用例 - 用户名为空/密码为空/用户名格式不正确

    @pytest.mark.parametrize("case",LD.wrong_datas)  # case = {"user": "", "passwd": "python", "check": "请输入手机号"},
    # @pytest.mark.parametrize("user,passwd,check", LD.wrong_datas)
    def test_login_failed_by_wrongData(self, case,init_driver):
        logging.info("******* 登陆功能 - 异常场景用例：数据格式校验 - 用户名为空/密码为空/用户名格式不正确 *******")
        # 调用登陆页面的。登陆行为。
        init_driver[1].login(case["user"], case["passwd"])
        # 断言 - 登陆页面 - 应当现提示信息：请输入手机号
        assert case["check"] == init_driver[1].get_error_msg()

    # 错误的密码
    def test_login_failed_by_wrong_passwd(self):
        logging.info("******* 登陆功能 - 异常场景用例：数据后台有效性校验 - 密码错误 *******")
        # 调用登陆页面的。登陆行为。
        self.lp.login("18684720553", "python11")
        # 断言 - 登陆页面 - 应当现提示信息：帐号或密码错误!
        self.assertEqual("帐号或密码错误!", self.lp.get_error_msg_from_dialog())



# @pytest.mark.usefixtures("init_driver")
# def test_aaaa():
#     assert True

