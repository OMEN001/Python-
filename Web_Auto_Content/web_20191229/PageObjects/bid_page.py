# 2、标页面 - 获取输入当中，投资前的用户余额
# 3、标页面 - 获取标的余额，投资前。
# 2、标页面 - 输入金额20000，点击投标
# 3、标页面 - 成功弹出框当中，点击查看并激活

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_20191229.PageLocators.bid_page_loc import BidPageLoc as loc

class BidPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 获取标的余额
    def get_bid_money(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.bid_money_text))
        return self.driver.find_element(*loc.bid_money_text).text

    # 投标
    def invest(self,invest_money):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.money_input))
        self.driver.find_element(*loc.money_input).send_keys(invest_money)
        self.driver.find_element(*loc.invest_button).click()

    # 点击 投资成功提示框 当中的  查看并激活按钮
    def click_active_button_in_success_popup(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.active_button_on_successPop))
        self.driver.find_element(*loc.active_button_on_successPop).click()