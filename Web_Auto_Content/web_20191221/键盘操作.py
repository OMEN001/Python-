# Keys

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启与浏览器的会话 - newSession
driver = webdriver.Chrome()
# 隐性等待 - 1）等待元素被找到  2）等待命令执行完成。
# driver.implicitly_wait(20)  # 最多等20秒。20秒内什么找到什么时候继续执行后续代码
driver.get("http://www.baidu.com")

# driver.find_element_by_id('kw').send_keys("柠檬班")
# driver.find_element_by_id("su").click()  # 点击 百度一下 按钮
driver.find_element_by_id('kw').send_keys("柠檬班",Keys.ENTER)

time.sleep(10)
driver.quit()