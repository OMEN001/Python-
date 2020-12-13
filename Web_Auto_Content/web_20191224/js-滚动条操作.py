"""
滚动的目标：为了让自己要操作的元素，到可视区域当中。

事情：将我要操作的元素，拖动到可视区域当中。

js语句：
滚动到可视区域的基本语法 ：
  element.scrollIntoView();

很多网页是可以自己去滚动到可视区域。

1、移动到元素element对象的“底端”与当前窗口的“底部”对齐：
     driver.execute_script("arguments[0].scrollIntoView(false);",element)

2、移动到元素element对象的“顶端”与当前窗口的“顶部”对齐  ：
     driver.execute_script("arguments[0].scrollIntoView();",element)

3、移动到页面底部：
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

4、移动到页面顶部：
     driver.execute_script("window.scrollTo(document.body.scrollHeight,
     0)")

# 函数： scrollIntoViewIfNeeded
"""

from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启与浏览器的会话 - newSession+
driver = webdriver.Chrome()
# 隐性等待 - 1）等待元素被找到  2）等待命令执行完成。
# driver.implicitly_wait(20)  # 最多等20秒。20秒内什么找到什么时候继续执行后续代码
driver.get("http://www.baidu.com")

# driver.find_element_by_id('kw').send_keys("柠檬班")
# driver.find_element_by_id("su").click()  # 点击 百度一下 按钮
driver.find_element_by_id('kw').send_keys("柠檬班",Keys.ENTER)

loc = (By.XPATH,'//a[text()=" - 主页"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
element = driver.find_element(*loc)


# 通过js将元素滚动到可视区域之后，再去点击。
    # # 执行js语句 的函数。arguments -- 列表
driver.execute_script("arguments[0].scrollIntoView(false);",element)
readonly = driver.execute_script("return arguments[0].readonly;",element)
time.sleep(2)
element.click()

time.sleep(10)
driver.quit()