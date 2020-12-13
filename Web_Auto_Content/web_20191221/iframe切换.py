"""
1、确认自己要操作的元素，是否在iframe当中？
   F12，定位元素后，看上方的完整的元素路径当中，是否有iframe，是否有2个以上的html

2、找到iframe - 标签对。容器，里面放的是html.
  iframe是个元素，主html来讲，仍然是可以通过元素定位找到的。
  3种方式：
  1）name属性：  login_frame_qq
  2）index下标：  2
  3）webElement对象：driver.find_element_by_name("login_frame_qq")

3、切换进iframe,在新的html页面当中操作。
4、若要退出iframe,driver.switch_to.default_content()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启与浏览器的会话 - newSession
driver = webdriver.Chrome()

# 等待
# 切换
driver.switch_to.frame("login_frame_qq")
driver.switch_to.frame(2)
driver.switch_to.frame(driver.find_element_by_name("login_frame_qq"))

# 切换之后，新的html就是根结点 。

# 一次回到解放前。default_html
driver.switch_to.default_content()

# 切换回上一个iframe页面
driver.switch_to.parent_frame()