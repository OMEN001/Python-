from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1、导入webdriver,实例化。
# 2、外部传参

class LoginPage:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    password_input = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button = (By.TAG_NAME, 'button')
    # 表单区域的 错误提示框
    error_from_login_form = (By.XPATH,'//div[@class="form-error-info"]')


    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 登陆行为
    def login(self,username,passwd):
        # 等待？？
        WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(self.login_button))
        # 输入用户名
        self.driver.find_element(*self.user_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(passwd)
        self.driver.find_element(*self.login_button).click()

    # 获取 表单区域的 错误提示信息
    def get_error_msg_from_login_form(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(self.error_from_login_form))
        return self.driver.find_element(*self.error_from_login_form).text



