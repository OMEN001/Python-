from selenium.webdriver.common.by import By


class LoginPageLoc:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    password_input = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button = (By.TAG_NAME, 'button')
    # 表单区域的 错误提示框
    error_from_login_form = (By.XPATH, '//div[@class="form-error-info"]')