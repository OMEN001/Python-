"""
============================
Author:柠檬班-木森
Time:2019/10/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import logging


class MyLogger(object):

    @classmethod
    def create_logger(cls):
        """创建日志收集器"""
        # 创建一个日志收集器
        my_log = logging.getLogger("musen")
        # 设置日志收集器的收集等级
        my_log.setLevel("DEBUG")
        # 设置日志输出的格式
        formater = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        # 创建一个输出导控制台的日志输出渠道
        sh = logging.StreamHandler()
        sh.setLevel("DEBUG")
        # 设置输出导控制台的格式
        sh.setFormatter(formater)
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(sh)

        # 创建一个输出导文件的渠道
        fh = logging.FileHandler(filename="test.log", encoding='utf8')
        fh.setLevel('DEBUG')
        # 设置输出导文件的日志格式
        fh.setFormatter(formater)
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(fh)
        return my_log


log = MyLogger.create_logger()



