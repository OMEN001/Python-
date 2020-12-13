"""
============================
Author:柠檬班-木森
Time:2019/9/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

s = "abc"

# res接收的就是id这个函数的返回值
# res = id(s)
# print(res)
#
# # 函数调用之后，返回的式None就代表函数没有返回值
# res2 = print('123')
# print(res2)
#
# res3 = type(s)
# print(res3)

# s1接收的是 字符串调用替换方法之后返回的内容
# s1 = s.replace('a', 'x')
# print(s1)
#
# li = [11, 2, 33]
# res = li.append(44)
# print(res)


# 函数中return  关键字  决定函数有没有返回值 以及函数返回的内容
# return:这个关键字只能在函数中使用，
# 作用： 1、返回结果（函数的返回值），2、结束函数的运行

def add_number():
    a = 100
    b = 200
    return 'abc'


# res1 = add_number()
# print(res1)


def add_number2():
    a = 100
    b = 200


# res3 = add_number2()
# print(res3)

def func3():
    li = [11, 22, 33]
    for i in li:
        if i == 22:
            return '找到了22'
        elif i == 33:
            return '找到了33'


res = func3()
print(res)
