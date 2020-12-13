

import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time
import datetime

from web_20191229.Common import logger

from selenium import webdriver

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self,loc,img_doc,timeout=20,poll_frequency=0.5):
        logging.info("{} 等待 {} 元素可见。".format(img_doc,loc))
        start_time = time.time()  # 开始等待的时间
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 输出异常信息
            logging.exception("等待元素可见失败")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise
        else:
            end_time = time.time()  # 结束等待的时间
            logging.info("起始时间：,结束时间：，等待时长：")

    # 查找元素
    def get_element(self,loc,img_doc):
        logging.info("{} 查找 {} 元素。".format(img_doc,loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            # 输出异常信息
            logging.exception("查找元素失败：")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise
        else:
            return ele

    # 点击操作
    def click_element(self,loc,img_doc,timeout=20,poll_frequency=0.5):
        # 1、元素可见；# 2、查找元素 # 3、元素的操作。
        self.wait_ele_visible(loc,img_doc,timeout,poll_frequency)
        ele = self.get_element(loc,img_doc)
        logging.info("{} 点击 {} 元素".format(img_doc,loc))
        try:
            ele.click()
        except:
            # 输出异常信息
            logging.exception("点击元素失败：")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise

    # 输入操作
    def input_text(self,loc,text,img_doc,timeout=20,poll_frequency=0.5):
        # 1、元素可见；# 2、查找元素 # 3、元素的输入操作。
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        logging.info("{} 在 {} 中输入文本值：{}".format(img_doc,loc,text))
        try:
            ele.send_keys(text)
        except:
            # 输出异常信息
            logging.exception("元素输入文本失败：")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise

    # 获取元素文本
    def get_text(self,loc,img_doc,timeout=20,poll_frequency=0.5):
        # 1、元素可见；# 2、查找元素 # 3、元素的输入操作。
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        logging.info("{} 获取元素 {} 的文本值。".format(img_doc,loc))
        try:
            value = ele.text
        except:
            # 输出异常信息
            logging.exception("获取元素的文本失败：")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise
        else:
            logging.info("文本值为：{}".format(value))
            return value

    # 获取元素的属性值
    def get_element_attribute(self,loc,attr_name,img_doc,timeout=20,poll_frequency=0.5):
        """

        """
        # 1、元素可见；# 2、查找元素 # 3、元素的输入操作。
        self.wait_ele_visible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        logging.info("{} 获取元素 {} 的 {} 属性值。".format(img_doc,loc,attr_name))
        try:
            value = ele.get_attribute(attr_name)
        except:
            # 输出异常信息
            logging.exception("获取元素的属性失败：")  # Error级别
            # 截图。命名要见名如义：截图的名称，就能够知道是在哪个页面哪个行为截的图。
            # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
            self._save_page_shot(img_doc)
            raise
        else:
            logging.info("属性值为：{}".format(value))
            return value

    # 获取当前url
    # 得到所有的窗口列表
    def get_window_handles(self):
        logging.info("获取当前打开的所有窗口")
        try:
            wins = self.driver.window_handles
        except:
            pass
        else:
            logging.info("窗口列表为：{}".format(wins))
            return wins

    # 切换到最新窗口？ 0）触发新窗口出现 1）获取窗口列表；2）切换到最后一个；
    def switch_to_new_window(self):
        time.sleep(2)
        wins = self.get_window_handles()
        logging.info("切换到最新的窗口：{}".format(wins[-1]))
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            pass

    # 切换到iframe
    # 切换到alert的处理
    # 上传？
    # 滚动条处理？

    def _save_page_shot(self,img_doc):
        # img_doc 命名格式：页面名称_行为名称_年月日时分秒.png
        file_name = "{}_{}.png".format(img_doc,"")  # 路径/页面名称_行为名称_年月日时分秒.png
        logging.info("截图保存在：{}".format(file_name))
        try:
            self.driver.save_screenshot(file_name)  # 文件名称格式当中不要有:/空格
        except:
            logging.exception("保存截图失败。")
        else:
            logging.info("保存截图成功。")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    loc = ("id","kw")
    button_loc = ("id","su")
    bp = BasePage(driver)
    bp.input_text(loc,"柠檬班","百度首页_输入搜索内容")
    bp.click_element(button_loc,"百度首页_点击搜索按钮")
    time.sleep(10)
    driver.quit()
