import pytest
from selenium import webdriver
import logging
from web_20200102.Common import logger

from web_20200102.PageObjects.login_page import LoginPage
from web_20200102.PageObjects.home_page import HomePage

from web_20200102.TestDatas import Common_Datas as CD
from web_20200102.TestDatas import login_datas as LD


@pytest.fixture   # 申明这是一个 夹测试函数的   前置和后置的fixture
def init_driver():   # 名字叫做：setup
    # 前置代码
    logging.info("=====我是测试用例 *** 通用 *** 的前置=====")
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    lp = LoginPage(driver)
    yield driver,lp   # 返回driver和lp变量
    # 后置代码
    logging.info("=====我是测试用例 *** 通用 *** 的后置=====")
    driver.quit()

@pytest.fixture("class")
def myClass():
    logging.info("=====我是测试类级别的前置=====")
    yield
    logging.info("=====我是测试类级别的后置=====")


# ==============作业：1、 用pytest的 fixture  去表达 投资用例 的前置后置 =================
# ============2、考虑，如何能够让  充值用例/提现用例    共享你的前置的后置 ===========
