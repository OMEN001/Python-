"""
============================
Author:柠檬班-木森
Time:2019/10/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
return:是用给函数返回结果
print:print是用吧数据输出到控制台

"""

# def func():
#     return 999
# res = func()


"""
列表（list） 元祖(tuple)  字符串转换(str)

字典：[['a','b'][11,22]]  ====>zip

"""
# li = [11,22,33]
# res = tuple(li)
# print(res)
#
# print(str(li))
#
#
# s = '[11,22,33]'
# # 通过eval识别字符串中的 python表达式
# print(eval(s))

"""
编码思维
分析需求：
实现这个需求 可以分为那几步来实现，分别用中文描述出来这几个步骤

先思考  再动手  

每一行代码写之前都要明确的知道这个代码是用来做什么的。



"""

"""
break:结束循环
continue


while  条件：
   循环体 


"""

"""
异常处理

try:
    有可能会发生异常
except 指定捕获的异常类型1 as 变量：
    对不会到的异常进行处理
except 指定捕获的异常类型2：
    对不会到的异常进行处理
else:
    没有发生异常，那么就会进入到else中来执行
finally:
    不管有没有异常，始终会执行



"""

"""
跨文文件路径引用
相对路径
绝对路径

跨文件导包处理：从项目路径往下导入(项目目录下的包和模块能够直接被导入)
from py23_05day import zy_04day

"""

"""
python中函数的参数可以是任意类型,


"""


def work1(f):
    print('work1')
    print(f)


import requests


def work2():
    print('work2')


# work1(999)

# def main():
#     work1()
#     work2()
#
# main()
"""
实例方法怎么调用？

实例对象.方法（）
实例对象.属性名


类属性：
类.属性
对象.属性

"""


class MyClass:
    attr = 999

    def __init__(self, name):
        self.name = name

    def skill1(self):
        print("方法1")

    def skill2(self):
        print('方法2')
        self.skill1()
        print(self.name)
        print(MyClass.attr)
        print(self.attr)


# m = MyClass('小明')

# m.skill2()

# s = MyClass('小红')
# s.skill2()


""""
函数的各种参数 混合使用


"""


def func_test(name, age, score=100, *args, **kwargs):
    print(name)
    print(age)
    print(score)
    print(args)
    print(kwargs)


# 调用的时候传参尽量 统一风格（要么都通过位置传参，要么使用关键指定参数名传参）
# func_test('小明', 18,88,88,99)

# func_test(name='小红',age=18,aa=9999,bb=888)

#  混合方式传参，先写位置  参数 再写关键字参数
# func_test('小明',age=18,score=99,aa=9999,bb=99999)
# li = ['小明',18,88,99,00]
#
# func_test(*li)



class BasePhone(object):
    """大哥大"""

    attr = "basephone的属性"

    def __init__(self,name):
        self.name = name

    def func(self):
        print('----func---')

# 2005
class Phone_V1(BasePhone):
    """功能机"""
    pass


i = Phone_V1(999)  # 创建对象的时候  通过init设置的name属性
print(i.name)


i.func()
print(i.attr)

