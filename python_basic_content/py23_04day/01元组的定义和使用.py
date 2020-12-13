"""
============================
Author:柠檬班-木森
Time:2019/9/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
元组



"""
# 列表
# li = [1, 2, 3]
# print(type(li))
# # 列表是可变类型元素，定义之后对列表内部的元素可以进行修改
li = [11]

# 元组

# 元组定义的时候，注意点：

# 如何去定义一个空元祖
tu1 = ()
print(type(tu1))

# 元组中只要一个元素时，如何定义
# tu2 = (11,)
# print(type(tu2))

# tu3 = 11,
# print(tu3,type(tu3))


# tu4 = tuple([11])
# print(type(tu4),tu4)


# # 元组中的数据可以是任意类型的
# tu = (1, 2, 3,'abc',[11,22,33])
# print(type(tu))
# # 元组是不可变类型元素，定义之后内部的元素是不可以进行修改的（没有增删查改的方法）

# # 元组下标取值
# print(tu[0])
#
# # 元组切片
# print(tu[:2])


# 元祖中的方法

# tu = (1, 2, 3,11, 22, 33,1,2,3,1,1,1)
# # count：
# print(tu.count(1))
# # index:
# print(tu.index(11))
# print(tu)



#  列表  字符串  元祖

# list（）:  可以将元组 或者字符串  转换为  列表

# tuple（）: 可以讲  列表 或者字符串   转换为 元祖


l = [11, 22, 33]
s = "abcaaa"
t = (1, 2, 3,2,)
#
# print(list(s))
# print(list(t))
#
# print(tuple(s))
# print(tuple(l))
# print('-----------------------')
# res = str(l)
# print(res,type(res))
# print(repr(res))


# 内置函数 len():获取数据的元素总数（长度）

print(len(l))
print(len(s))
print(len(t))

