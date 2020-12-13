"""
============================
Author:柠檬班-木森
Time:2019/10/10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
为什么代码中会有浅色的波浪线   和红色的波浪线
浅色的波浪线：pycharm监测到你的这行代码不符合pep8规范（官方给出的编码规范）
红色的波浪线：pycharm监测到这行代码语法有问题 或者变量找不到（没有被定义）

"""

# 方式一：导入整个模块
# import test01
#
# print(test01.a)
# test01.work()


# 方式二：导入模块中的部分内容

# from test01 import a
# print(a)
# import test01
# from test01 import work  # 这个波浪线并不是代码写错了 知识pycharm识别不出我们自定义的这个模块

# work()

# 扩展
# 通过as给导入进来的方法或变量 重启起个名字（别名）
# from test01 import work as w1

# def work():
#     print('test02中的work')
#
# work()
# w1()

# import test01 as t1

# print(t1.a)
# t1.work()

# 导入多个内容
# from test01 import a,work,num
# print(a)
# print(num)

# 导入模块中所有的内容（不推荐使用）
# from test01 import *
# print(a)
# print(num)
# work()

