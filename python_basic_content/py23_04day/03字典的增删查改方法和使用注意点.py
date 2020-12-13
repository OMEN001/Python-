"""
============================
Author:柠檬班-木森
Time:2019/9/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
字典
字典中的数据，每条都是由键值对组成(key:value)
key:只能是不可变类型的数据（尽量用字符串）
value:可以是任意类型的数据




不可变类型的数据： 数值类型、字符串、元组
可变类型的数据：列表  字典、集合

"""

# dic = {"name": "小明"}

# 空字典的定义
# dic1 = {}
# print(dic1,type(dic1))

# 字典的增删查改方法

# 字典中添加元素
# 通过键进行赋值： dic[key] = 值
# dic['age'] = 18
# print(dic)

# 字典中修改元素(字典中的key是唯一的，不能重复)
# dic['age'] = 188
# print(dic)

# 一句话总结添加和修改 ：无则增 有则改


# 字典中查找元素
# 第一种：通过键去找对应的值（当查找的键不存在时，会报错）
# n = dic['name']
# print(n)

# 第二种：dic.get(key)（当查找的键不存在时，返回的是None）
# n = dic.get('name1')
# print(n)


# 字典中删除元素
# dic = {'aa': 11, "bb": 22, "cc": 33}

# pop方法:指定键去删除键值对
# res1 = dic.pop("cc")
# print(res1)
# print(dic)
#

# popitem:删除字典中最后一个键值对（python3.6起删除的是最后一个键值对）
# res = dic.popitem()
# print(res)
# print(dic)

# del关键字 进行删除
# del dic['cc']


# 字典中常用的其他的几个方法
dic = {'aa': 11, "bb": 22, "cc": 33}
# keys:获取所有的键
print(list(dic.keys()))

# values：获取所有的值
print(list(dic.values()))

# items: 获取所有的键值对，每个键值对是一个元组的形式
print(list(dic.items()))





