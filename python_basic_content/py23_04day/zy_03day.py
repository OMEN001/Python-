

"""
1.将给定字符串的PHP替换为Python      
  best_language = "PHP is the best programming language in the world! "

2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，
如果输入的数字是6或7则为周末，打印输出“今天是周几” 

3、现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过相关的操作改成li2 = [0，1，2，3，66,5，11，22，33]，
     第二步：对li2进行排序处理 


4、切片 
      1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
      2、s = 'python java php',通过切片获取: ‘java’ 
   

5、写出上课讲的 列表的所有方法 ，并说明  每个方法有什么作用


"""

# 第一题
best_language = "PHP is the best programming language in the world! "
str4 = best_language.replace('PHP', 'python')
print(str4)

# 第二题
# li = ['周一','周二','周三','周四','周五','周末','周末']
# num = int(input('请输入1-7:'))
# index = num-1
# data = li[index]
# print('今天是:{}'.format(data))

# 第三题
li2 = [1, 2, 3, 4, 5]

# 第一步
li2.insert(0, 0)  # 在最前面加入0
li2[4] = 66
li2.extend([11, 22, 33])  # 在最后加入三个元素
print(li2)

# 第二步：从小到大排序
li2.sort()
print(li2)

# 第四题
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

s = 'python java php'
print(s[7:11])

# 第五题
"""
添加元素：
append:往列表尾部添加元素
insert:通过下标指定位置插入元素
extend:添加多个元素(多个元素放在列表中)
删除元素：
remove:删除指定的元素
pop: 删除指定下标位置的元素
clear:清空列表（删除列表中所有的元素）

修改元素值：
通过下标修改指定元素的值

查找的方法：
index:返回指定元素的下标
count：查找元素出现的次数

其他的方法：
copy：用来复制列表的
sort:排序（默认从小到大）
reverse:反序
"""
