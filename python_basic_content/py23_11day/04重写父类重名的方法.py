"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
重写父类的方法:（父类有一个方法，继承之后,又定义了一个和父类方法名相同的方法）
直接调用重写之后的方法，直接调用自身有的这个方法（不会去父类找）


在方法中掉父类被重写的方法：
方式一：父类名.方法名（）
方式二：super().方法名（）



"""


class BasePhone(object):
    """大哥大"""

    def __init__(self, name):
        self.name = name

    def call_phone(self):
        print('打语音电话的功能Base')


# 2005
class Phone_V1(BasePhone):
    """功能机"""
    def call_phone(self):
        print('打语音电话的功能V1')

    def send_msg(self):
        print('发送短信')

    def music(self):
        print('播放音乐')


# 2015

class Phone_V2(Phone_V1):
    """智能机"""

    # 重写父类的方法（父类有一个方法，继承之后有定义了一个和父类方法名相同的方法）
    def call_phone(self):
        print('拨打视频电话')
        print('时间过去了5分钟')
        # 在方法中掉父类被重写的方法
        # 方式一：类名.方法名（self）
        # BasePhone.call_phone(self)
        # 方式二：super().方法名（）
        super().call_phone()

    def game(self):
        print('玩游戏')

    def qq(self):
        print('聊aa')


v2 = Phone_V2('华为p30')

v2.call_phone()