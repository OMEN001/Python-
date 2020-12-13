"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 1990
class BasePhone(object):
    """大哥大"""

    def call_phone(self):
        print('打电话的功能')


# 2005
class Phone_V1(object):
    """功能机"""

    def call_phone(self):
        print('打电话的功能')

    def send_msg(self):
        print('发送短信')

    def music(self):
        print('播放音乐')

# 2015

class Phone_V2(object):
    """智能机"""
    def call_phone(self):
        print('打电话的功能')

    def send_msg(self):
        print('发送短信')

    def music(self):
        print('播放音乐')

    def game(self):
        print('玩游戏')

    def qq(self):
        print('聊aa')
