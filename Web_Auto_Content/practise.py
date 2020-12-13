# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# #使用前进后退的方式切换页面
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# time.sleep(1)
#
# driver.get("http://www.taobao.com")
# time.sleep(1)
#
# driver.back()
# time.sleep(1)
#
# driver.forward()
# time.sleep(1)
#
# driver.refresh()



# #有些页面的链接打开后，会重新打开一个窗口（如进入天猫点击某个连接在当前浏览器的基础上打开另一个窗口）
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
#
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("京东")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# driver.find_element(By.XPATH,"//div[contains(@class,'ec-pc_title')]").click()
#
# #获取当前窗口的所有句柄
# win = driver.window_handles
# print("当前所有的句柄：",win)
# #获取当前句柄
# wins = driver.current_window_handle
# print("当前所有的句柄：",wins)
# #句柄切换
# driver.switch_to.window(win[0])
# time.sleep(2)
#
# driver.quit()


# #iframe 窗口切换
# driver = webdriver.Chrome()
# driver.get("https://ke.qq.com/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[@id='js_login']").click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//div[@class="content-btns"]//a[text()="QQ登录"]').click()
# time.sleep(1)
#
# driver.switch_to.frame("login_frame_qq")
#
# time.sleep(1)
# driver.find_element(By.XPATH,'//a[@id="switcher_plogin"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//input[@id="u"]').clear()
# driver.find_element(By.XPATH,'//input[@id="u"]').send_keys("2586089125")
# time.sleep(1)
# driver.find_element(By.XPATH,'//input[@id="p"]').clear()
# driver.find_element(By.XPATH,'//input[@id="p"]').send_keys("y2.13654654")
# time.sleep(1)
# driver.find_element(By.XPATH,'//input[@id="login_button"]').click()
# time.sleep(5)
# driver.quit()

# # #alert窗口切换
# driver = webdriver.Chrome()
# driver.get("E:\Lemon_Api_Web_Content\Web_Auto_Content\my_first.html")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[@id="cc"]').click()
# time.sleep(2)
#
# al = driver.switch_to.alert
#
# # 关闭
# # al.accept()  # 确定
# # # al.dismiss()  # 取消
# print(al.text)  # 获取 文本内容
# # # al.send_keys("") # 输入内容
# driver.quit()


#日期输入框处理
# driver = webdriver.Chrome()
# driver.get("https://www.12306.cn/index/")
# driver.maximize_window()
# time.sleep(1)
# js_pha = 'var a = document.getElementById("fromStationText");a.value="上海";' \
#          'var b = document.getElementById("fromStation"); b.value="SHH";'
#
# driver.execute_script(js_pha)
# js_pha_1 = 'var a = document.getElementById("train_date");a.readOnly = false;a.value = "2019-06-15";'
# driver.execute_script(js_pha_1)
# time.sleep(5)
# driver.quit()





