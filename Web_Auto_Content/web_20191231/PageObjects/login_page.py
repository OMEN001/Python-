

from web_20191228.PageLocators.login_page_locs import LoginPageLoc as loc
from web_20191229.Common.basepage import BasePage


# 1、导入webdriver,实例化。
# 2、外部传参

class LoginPage(BasePage):

    # 登陆行为
    def login(self,username,passwd):
        self.input_text(loc.user_input,username,"登陆页面_输入用户名")
        self.input_text(loc.password_input,passwd,"登陆页面_输入密码")
        self.click_element(loc.login_button,"登陆页面_点击登陆按钮")

    # 获取 表单区域的 错误提示信息
    def get_error_msg_from_login_form(self):
        return self.get_text(loc.error_from_login_form,"登陆页面_获取登陆表单区域的错误提示信息")


