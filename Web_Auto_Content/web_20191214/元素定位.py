from selenium import webdriver
import time

# 打开对应的浏览器，开启与浏览器之间的会话。
# 非常干净的浏览器。没有任何的用户数据。
driver = webdriver.Chrome()  # 接口：newSession # 封装了一系列对网页的操作指令

driver.get("http://www.baidu.com")    # http

"""
元素在页面的3种状态：
1）存在：能够找到。
2）可见：在浏览器呈现的页面当中，可以看到它的大小。有高和宽。
3）可用：特别关注输入框和按钮。
1） -》 2） -》 3）
"""

# 按照元素本身的特征来找。
# 8个元素定位方式 ： 1类(6个)：只根据元素的一个特征来找。 2类：多种组合：xpath,css选择器
# id,name,className,tagName,link,partial_link
# id: 固定不变。动态变化 的id。
ele = driver.find_element_by_id("kw")  # 找元素。下一步动作：操作。对象：WebElement(属性+操作)
ele.send_keys("柠檬班")
"""
1) 属性
2）操作：查找子元素？  基于当前元素的所有后代。
基本操作：1）点击 click  2）输入   send_keys   3) 获取属性 get_attribute   4) 获取文本：.text
"""
# 2、tag_name 标签名称
# ele = driver.find_element_by_tag_name("input")  # 一个WebElement对象.第一个
# eles = driver.find_elements_by_tag_name("input")  # 列表。所有匹配的元素。

# # 3、class_name  class属性
# driver.find_element_by_class_name("bdsug") #一个类名。
# driver.find_elements_by_class_name("bdsug")
#
# # 4、name属性
# driver.find_element_by_name("wd")
# driver.find_elements_by_name("wd")

# # 5、6  只针对a元素
# driver.find_element_by_link_text("更多产品")
# driver.find_element_by_partial_link_text("产品")

# 7、xpath
"""
//*[@id="kw"]
/html/body/div[2]/div[1]/div/div[1]/div/form/span[1]/input
/html/body/div[2]/div/form/div[1]/input

绝对定位：以/开头   父/子   完整的路径、绝对的位置
相对定位：1）相对于谁？参照物    以//开头    确认：有还是没有匹配的元素？
          //标签名(一级筛选)
          
          //标签名[@属性名称=值]   //*[@属性名称=值]
          逻辑运算：and or    //标签名[@属性名称=值 and @属性名称=值]
          文本定位：//标签名[text()=文本值]
          包含定位：//标签名[contains(@属性,值)]   //标签名[contains(text(),值)]
          
          层级定位：//div[@id="u1"]//a[@name="tj_login"]
"""
