"""
============================
Author:柠檬班-木森
Time:2019/10/8
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


#  * 用来接收位置参数的不定长参数
#  **  是用来接收关键字参数的不定长参数

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)


# data = [11, 22, 33, 44, 55]
# 通过*对元祖拆包，只要在调用函数的时候可以用（用在函数的参数上）
# func(*data)


def func1(a, b, c):
    print(a)
    print(b)
    print(c)


data = [11, 22, 33]
# func1(*data)

# aa, bb, cc = data
# print(aa,bb,cc)



