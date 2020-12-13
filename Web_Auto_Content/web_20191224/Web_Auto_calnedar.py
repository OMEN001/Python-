#_*_conding:utf-8_*_
#@Time    :2019/12/2321:45
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait   #引入等待类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.12306.cn/index/")
driver.maximize_window()

set_out = "var a = document.getElementById('fromStationText');a.value='北京';"
set_out_1 = "var b = document.getElementById('fromStation');b.value='BJP';"
driver.execute_script(f"{set_out};{set_out_1}")
time.sleep(2)
arrived = "var c = document.getElementById('toStationText');c.value= '兰州';"
arrived_1 = "var d = document.getElementById('toStation');d.value= 'LZP';"
driver.execute_script(f"{arrived};{arrived_1}")
time.sleep(2)
date = "var e = document.getElementById('train_date');e.readOnly=false;e.value='2020-01-21';"
driver.execute_script(date)

loc = (By.ID,'search_one')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
time.sleep(0.5)
driver.find_element(*loc).click()

time.sleep(5)

driver.quit()