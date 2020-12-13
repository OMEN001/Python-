import pytest
from selenium import webdriver
import logging
from Common import logger

from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage

from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD


@pytest.fixture   # 申明这是一个 夹测试函数的   前置和后置的fixture
def init_driver():   # 名字叫做：setup
    # 前置代码
    logging.info("=====我是测试用例 *** 通用 *** 的前置=====")
    driver = webdriver.Chrome()
    driver.get(CD.login_url)
    # lp = LoginPage(driver)
    yield driver   # 返回driver
    # 后置代码
    logging.info("=====我是测试用例 *** 通用 *** 的后置=====")
    driver.quit()
# ==============作业：1、 用pytest的 fixture  去表达 投资用例 的前置后置 =================
# ============2、考虑，如何能够让  充值用例/提现用例    共享你的前置的后置 ===========
"""
登陆用例: 打开浏览器，访问登陆页面                  后置 ：关闭浏览器
投资用例：打开浏览器，访问登陆页面，登陆操作         后置 ：关闭浏览器

当用例当中，调用setup的时候：
init_driver的前置：打开浏览器，访问登陆页面 
setup的前置：登陆操作
 *** 测试用例  ***
setup的后置：无
init_driver的后置：关闭浏览器
"""
from PageObjects.bid_page import BidPage

@pytest.fixture
def setup(init_driver):  # “继承”，只能“继承”同级或者比自己级别高的。
    LoginPage(init_driver).login(CD.user, CD.passwd)
    yield init_driver



# ============== class级别 =================
@pytest.fixture("class")
def myClass():
    logging.info("=====我是测试类级别的前置=====")
    yield
    logging.info("=====我是测试类级别的后置=====")

# ====== session级别 =========
@pytest.fixture(scope="session",autouse=True)
def mySession():
    logging.info("=====我是 -- 测试会话 -- 级别的前置=====")
    yield
    logging.info("=====我是 -- 测试会话 -- 别的后置=====")


# ====== module级别 =========
@pytest.fixture(scope="module")
def myModule():
    logging.info("=====我是 -- 测试模块py文件 -- 级别的前置=====")
    yield
    logging.info("=====我是 -- 测试模块py文件 -- 别的后置=====")
