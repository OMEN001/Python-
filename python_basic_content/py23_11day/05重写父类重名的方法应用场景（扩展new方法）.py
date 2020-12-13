"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
__new__方法：创建对象的
Create and return a new object

面向对象的三大特性:
继承：
封装：
多态：鸭子类型



"""


class Obj(object):

    def __new__(cls, *args, **kwargs):
        res = super().__new__(cls)
        return res



o = Obj()
print(o)



