"""
============================
Author:柠檬班-木森
Time:2019/10/8
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

#  enumerate
# li = [11,22,33,44]
#
# res = enumerate(li)
#
# list2 = list(res)
# print(list2)
#
#
# dic = {"a":11,"b":22}
# # print(list(dic.items()))


# eval:识别字符串中的python表达式

# s1 = "(1,2,3)"
# s2 = "[11,22,33]"
#
# print(s1, type(s1))
#
# #  识别字符串中元祖
# res11 = eval(s1)
# print(res11, type(res11))
#
# # 识别字符串中的列表
# res2 = eval(s2)
# print(res2, type(res2))

# 注意点：如果是个纯粹的字符串，那么使用eval进行转换之后就变成了一个变量名
# python = 666
# s4 = "python"
# res4 = eval(s4)
# print(res4,type(res4))


# 过滤函数:filter(参数1，参数2)
# 参数1：函数
# 参数2：待过滤的数据

#  案例 li = [11,22,33,44,1,2,3,4,5,77,2,323,90]

# 过滤所有大于33的数据

# li = (11, 22, 33, 44, 1, 2, 3, 4, 5, 77, 2, 323, 90)
#
# def func(x):
#     return x > 33
#
# # 方式一
# new_list = []
# for i in li:
#     if func(i):
#         new_list.append(i)
#
# # 方式二
# new_list = filter(func, li)
#
#
# print(list(new_list))


# 扩展
# 匿名函数:
# new_list = filter(lambda x:x>33, li)


# zip聚合打包的函数

#
# li = [11,22,33,44]
# li2 = [111,222,333,444]
# li3 = [111111,22222,33333,44444]
#
# res5 = zip(li,li2,li3)
#
# print(list(res5))


#  案例：
# users_title = ["name", "age", "gender"]
#
# users_info = [['小明', 18, '男'],
#               ["小李", 19, '男'],
#               ["小美", 17, '女']
#               ]
#
# # 要求：将上述数据转换为以下格式
# users = [{'name': '小明', 'age': 18, 'gender': '男'},
#          {'name': '小李', 'age': 19, 'gender': '男'},
#          {'name': '小美', 'age': 17, 'gender': '女'}]
#
# #
# new_users = []
# for user in users_info:
#     data = zip(users_title, user)
#     new_users.append(dict(data))
#
# print(new_users)

# t = ["name", "age", "gender"]
# s = ['小明', 18, '男']
#
# res = zip(t,s)
# print(dict(res))


# import keyword
#
# print(keyword.kwlist)

