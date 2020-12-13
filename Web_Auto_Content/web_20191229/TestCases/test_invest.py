import unittest
from selenium import webdriver
import time

from web_20191228.PageObjects.login_page import LoginPage
from web_20191228.PageObjects.home_page import HomePage
from web_20191229.PageObjects.bid_page import BidPage

from web_20191228.TestDatas import Common_Datas as CD
from web_20191228.TestDatas import login_datas as LD

class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 打开浏览器
        # 登陆操作
        # 调用接口 - 加标/用户充值
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 访问 系统登陆页面
        self.driver.get(CD.login_url)
        LoginPage(self.driver).login(CD.user,CD.passwd)

    def tearDown(self) -> None:
        pass

    def test_invest_success(self):
        """
        正向场景 - 投资成功：投资金额固定为20000
        """
        # 步骤
        # 1、首页 - 第一标 - 抢投标
        HomePage(self.driver).click_first_bid()
        # 2、标页面 - 获取输入当中，投资前的用户余额
        bp = BidPage(self.driver)
        user_money_before_invest = bp.get_user_money()
        # 3、标页面 - 获取标的余额，投资前。
        bid_money_before_invest = bp.get_bid_money()
        # 2、标页面 - 输入金额20000，点击投标
        bp.invest("20000")
        # 3、标页面 - 成功弹出框当中，点击查看并激活
        bp.click_active_button_in_success_popup()
        # 断言
        # 1、用户余额少了20000
        # 个人页面 - 获取用户当前的余额 - 投资后
        # 2、标的可投余额少了20000
        # 个人页面 - 回退到上一页，刷新页面。
        # 标的页面 - 获取标的余额
        pass


