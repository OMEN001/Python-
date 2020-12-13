"""
============================
Author:柠檬班-木森
Time:2019/9/21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
列表：
可变类型的数据：定义之后可以往这个数据中添加，删除，修改元素



"""

# li = ['MUSEN', 18, '男']

# 下标取值
# print(li[2])
# 切片
# print(li[0:2])


# 列表的增删查改方法

# 添加数据
li = ['MUSEN', 18, '男']
# append方法：往列表的结尾处添加元素
li.append([11,22,33])
# insert方法：通过指定位置插入数据:第一个参数时插入的下标位置，第二个参数是插入的值
# li.insert(0,666)
# extend方法：可以往列表中一次性添加多条数据(了解)
li.extend(['aa','bb',888])
li.extend('AAA')
print(li)


# 删除数据
# li2 = [11,22,33,44,55,'aa',11]
# remove：删除指定的元素
# li2.remove('aa')

# pop方法:默认删除最后一个元素（可以指定下标位置进行删除）
# li2.pop(0)

# clear 清空列表的方法
# li2.clear()

# 关键字del 删除
# del li2[6]
# print(li2)


# 查询的方法
# li3 = [11,22,33,44,55,'aa',11]

# 下标取值

# index方法:找到第一个配置的元素 返回结果， 没找到会报错(了解)
# res = li3.index(111)
# print(res)

# count:获取某个元素的数量
# res2 = li3.count(11)
# print(res2)


# 修改元素：

# 通过下标找到元素进行重新赋值
# li3 = [11,22,33,44,55,'aa',11]
#
# li3[5] = 66
# li3[4] = 77
# li3[2],li3[1] = 111,222
# print(li3)


# 其他的方法

li5 = [11, 222, 232, 43, 55, 6, 7777, 8]
#     [8, 7777, 6, 55, 43, 232, 222, 11]

# sort方法：排序 (默认升序,加参数reverse=True，按降序进行排序)
# li5.sort()

# reverse

# 将列表反序
li5.reverse()

# print(li5)


# copy方法
li6 = [11, 222, 232, 43, 55,'jhh',['jgg']]

li7 = li6
li8 = li6.copy()

print(id(li6))
print(id(li7))
print(id(li8))

li6.append(99999999999)


print(li6)
print(li7)
print(li8)
