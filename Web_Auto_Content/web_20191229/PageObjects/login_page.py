
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_20191228.PageLocators.login_page_locs import LoginPageLoc as loc


# 1、导入webdriver,实例化。
# 2、外部传参

class LoginPage:


    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 登陆行为
    def login(self,username,passwd):
        # 等待？？
        WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(loc.login_button))
        # 输入用户名
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.password_input).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()

    # 获取 表单区域的 错误提示信息
    def get_error_msg_from_login_form(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(loc.error_from_login_form))
        return self.driver.find_element(*loc.error_from_login_form).text



