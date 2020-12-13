"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
类方法：可以由类去调用，也可以由实例对象去调用
    类方法的第一个参数cls:代表的是类本身
    
静态方法：静态方法可以由类去调用，也可以由对象去调用

实例方法：只能由实例对象去调用

"""


class MyClass:
    #  类属性
    # 公有属性
    attr = 100
    # 私有属性（声明为私有属性之后，不要在类外面通过对象或者是类去使用这个属性）
    _attr = 999
    __attr = 99999

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    # 实例方法
    def func1(self):
        print(self)
        print('实例方法1')

    # 类方法
    @classmethod
    def c_func(cls):
        print(cls)
        print('类方法c_func')

    # 静态方法
    @staticmethod
    def s_func():
        print('这个是静态方法')


m = MyClass('musen', 18)
# 实例方法的调用
# m.func1()

# 类方法的调用
# m.c_func()
# MyClass.c_func()


# 静态方法的调用

# MyClass.s_func()
# m.s_func()


