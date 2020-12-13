
js_pha = 'var a = document.getElementById("train_date");a.readOnly = false;a.value = "2010-01-22";'

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
# driver.get("http://www.baidu.com")

# 获取今天+10天以后的日期，转换成 XXXX-XX-XX
driver.execute_script(js_pha)