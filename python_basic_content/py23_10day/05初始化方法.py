"""
============================
Author:柠檬班-木森
Time:2019/10/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""定义在类里面的函数：叫做方法（本质上还是函数）



初始化方法：
    创建对象的时候自动执行的，不需要手动调用这个方法


self：代表的就是对象(谁去调用这个方法，代表的就是谁)

"""


class Cat:
    """
    定义一个猫类
    """
    # 类属性
    teg = "四条腿"
    tail = "有尾巴"

    # 定义实例属性通过初始化方法（__init__）来定义
    def __init__(self, age, name):
        # 定义实例属性，
        print(self)
        self.age = age
        self.name = name
        print("正在给对象设置属性")


# 创建对象
kt = Cat(age=18,name="凯蒂")
print(kt)

hh = Cat(age=20,name='灰灰')
print(hh)
#
# print(kt.age,kt.name,kt.teg)









