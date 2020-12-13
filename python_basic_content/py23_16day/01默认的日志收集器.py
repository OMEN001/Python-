"""
============================
Author:柠檬班-木森
Time:2019/10/29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


"""
日志模块:logging(python中的官方库)

logging模块中默认的日志收集器：root

日志默认收集等级位：warning以上

"""

import logging

# 创建一个日志收集器，如果没有传参数，则返回默认的日志收集器（root）
my = logging.getLogger()

# my.setLevel('DEBUG')


a = 100
print('调试数据',a)

logging.debug("这个是debug输出的调试信息a:{}".format(a))
logging.info("这个是debug输出的调试信息")
logging.warning("这个是debug输出的调试信息")
logging.error("这个是debug输出的调试信息")
logging.critical("这个是debug输出的调试信息")

