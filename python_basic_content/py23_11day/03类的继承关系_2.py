"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类属性可以直接继承

实例方法通过继承可以得到



实例属性能不能继承？
    实例属性时实例对象所独有的(创建实例对象的时候才会进行赋值)



"""



# 1990
class BasePhone(object):
    """大哥大"""

    attr = "basephone的属性"

    def __init__(self,name):
        self.name = name

    def call_phone(self):
        print('打电话的功能')


# 2005
class Phone_V1(BasePhone):
    """功能机"""

    def send_msg(self):
        print('发送短信')

    def music(self):
        print('播放音乐')

# 2015

class Phone_V2(Phone_V1):
    """智能机"""

    def game(self):
        print('玩游戏')

    def qq(self):
        print('聊aa')


# print(Phone_V2.attr)

# p1 = Phone_V2('华为P30')
# p1.call_phone()
# # p1.send_msg()
# # p1.game()
# # print(p1.name)

b1 = BasePhone('大哥大')
v1 = Phone_V1('oppo音乐手机')
p1 = Phone_V2('华为P30')

print(p1.name)
print(b1.name)
print(v1.name)