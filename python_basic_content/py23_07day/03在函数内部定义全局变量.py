"""
============================
Author:柠檬班-木森
Time:2019/10/8
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""


"""


# def func():
#     global b  #  在函数内部声明全局变量
#     b = 100
#
# func()
#
#
# print(b)


#  扩展知识点


def func():
    aa = 11

    def func2():
        nonlocal aa  # 使用nonlocal声明外部函数的局部变量，可以在嵌套函数内部修改外部函数的局部变量的值
        aa +=1
        print(aa)
    func2()
    print(aa)


func()

# print(aa)