from selenium import webdriver
import time

# 打开对应的浏览器，开启与浏览器之间的会话。
# 非常干净的浏览器。没有任何的用户数据。
driver = webdriver.Chrome()  # 接口：newSession # 封装了一系列对网页的操作指令

driver.get("http://www.baidu.com")    # http

# 浏览器最大化
driver.maximize_window()
# # 设置
# driver.set_window_size()
driver.get("http://www.taobao.com")  # 第二个页面

# 后退
driver.back()  # www.baidu.com
time.sleep(2)
# 前进
driver.forward()  # 历史记录
time.sleep(2)
# 刷新
driver.refresh()


# driver.close()  # 关闭当前窗口。
# # 退出会话。关闭浏览器，关闭chromedirver
driver.quit()
