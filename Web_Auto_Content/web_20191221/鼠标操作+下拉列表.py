"""
actionChains -
点击   click
双击   double_click
悬浮   move_to_element
右键   context_click
拖拽   drag_and_drop
暂停   pause

click_and_hold  和  release

0) 实例化actionChains类
1) 要操作的动作放在 链表当中。  动作的函数 - 放到列表当中。(找到元素，调用鼠标行为)
2) 调用perform() 去执行动作。
"""
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.select import Select

# 开启与浏览器的会话 - newSession
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 设置元素
loc = (By.XPATH,'//div[@id="u1"]//a[@name="tj_settingicon"]')

# driver.find_element(*loc).click()

# 0) 实例化actionChains类
ac = ActionChains(driver)

# 1) 要操作的动作放在 链表当中。
ele = driver.find_element(*loc)
ac.move_to_element(ele).pause(0.5).click(ele)

# 2) 调用perform() 去执行动作。
ac.perform()

# 等待高级搜索出现
loc = (By.XPATH,'//a[text()="高级搜索"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# select下拉列表：select/option
# 1）实例化Select类 - select元素
loc = (By.XPATH,'//select[@name="ft"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
select_ele = driver.find_element(*loc)
s = Select(select_ele)

# 2）使用它提供的选择方法，选择下拉列表的值
"""
1) 下标。  s.select_by_index()
2) 文本。  s.select_by_visible_text()
3) value属性  s.select_by_value()
"""
s.select_by_index(6)
time.sleep(3)
s.select_by_visible_text("Adobe Acrobat PDF (.pdf)")
time.sleep(3)
s.select_by_value("ppt")



time.sleep(10)
driver.quit()