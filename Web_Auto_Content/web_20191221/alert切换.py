"""
弹出框 ：
   html弹框： selenium webdriver
   非html弹框：
alert是什么？？ --- alert、confirm、prompt

1、某一个行为，触发了alert弹框

2、关闭它！！！ Alert类处理。
   1）切换到alert

3、继续html页面的操作。

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 开启与浏览器的会话 - newSession
driver = webdriver.Chrome()
driver.get('file:///D:/Pychram-Workspace/py23_web_study/web_20191221/my_first.html')

# 1、某一个行为，触发了alert弹框
driver.find_element_by_id("cc").click()

time.sleep(1)
# 切换
al = driver.switch_to.alert

# 关闭
al.accept()  # 确定
# al.dismiss()  # 取消
# al.text  # 获取 文本内容
# al.send_keys("") # 输入内容

# 继续页面操作
