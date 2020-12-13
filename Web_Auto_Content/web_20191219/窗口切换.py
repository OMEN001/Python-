"""
你怎么要切换到哪儿？？

1）有一行为，触发了新的窗口出现
2）获取所有的窗口handles --- 列表。 按照窗口出现的顺序。最新的窗口是最后一个。
3）切换：switch_to.window(新窗口的handle)
   从一html页面，切换到另外一个html页面。
"""

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

driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id("su").click()

loc = (By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))

driver.find_element(*loc).click()  # 打开了新的窗口
time.sleep(1)

# 获取句柄
wins = driver.window_handles
print("当前所有的句柄：",wins)
# 可以获取当前窗口的句柄
cur = driver.current_window_handle
print("当前所有的句柄：",wins)

# 切换
driver.switch_to.window(wins[-1])

loc=(By.XPATH,'//ul[@id="js-tab"]//h2[contains(text(),"老师")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()   # 打开 老师  选项