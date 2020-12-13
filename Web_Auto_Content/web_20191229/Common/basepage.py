
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time
import datetime

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
    loc = ("id","kww")
    bp = BasePage(driver)
    bp.wait_ele_visible(loc,"百度首页_搜索输入框",timeout=10)
