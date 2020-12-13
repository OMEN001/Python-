"""
1、为什么要等待？
   你要操作的元素，尚未加载出来。  看不见，没法下一步操作。
   1）后台数据请求，
   2）网络很慢
   3）页面渲染

2、如何等？  功能测试 - 什么时候出现了什么操作？ 智能。

3种方式：
1）傻等。 time.sleep(指定时间秒)  20分钟。

2）智能等待方式： 什么时候出现什么时候就停止等待。等待的上限。万一上限到了还未等待，timeoutException
   1) implicity_wait
   2）显性等待：所有条件都是明确指出来的。等待条件存在之后，再进行后续的代码执行。
      等待：WebdriverWait   条件：expected_condition
      等待20秒   检测条件成立的间隔：默认是0.5秒


什么时候要等待？
   元素操作之前，都请等一等。


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

# 动作： 点击登陆链接
loc = (By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')
driver.find_element(*loc).click()

# 1、等待元素可见？？  等待匹配到的所有元素可见？？
# 2、url改变？新的窗口出现？。。。。
# 等待XXx元素可见
# 1、元素定位表达式
loc = (By.ID,'TANGRAM__PSP_10__footerULoginBtn')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
time.sleep(0.5)  # 辅助作用。
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
driver.find_element_by_id('TANGRAM__PSP_10__userName').click()

time.sleep(5)

# 结束会话
driver.quit()
