# 2、标页面 - 获取输入当中，投资前的用户余额
# 3、标页面 - 获取标的余额，投资前。
# 2、标页面 - 输入金额20000，点击投标
# 3、标页面 - 成功弹出框当中，点击查看并激活

from web_20191229.PageLocators.bid_page_loc import BidPageLoc as loc
from web_20191229.Common.basepage import BasePage

class BidPage(BasePage):

    # 获取用户余额
    def get_user_money(self):
        return self.get_element_attribute(loc.money_input,"data-amount","标页面_获取用户余额")

    # 获取标的余额
    def get_bid_money(self):
        return self.get_text(loc.bid_money_text,"标页面_获取标余额")

    # 投标
    def invest(self,invest_money):
        self.input_text(loc.money_input,invest_money,"标页面_输入投资金额")
        self.click_element(loc.invest_button,"标页面_点投资按钮")


    # # 点击 投资成功提示框 当中的  查看并激活按钮
    # def click_active_button_in_success_popup(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.active_button_on_successPop))
    #     self.driver.find_element(*loc.active_button_on_successPop).click()