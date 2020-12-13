
"""
一、有5道题（通过字典来操作）：
    1. 某比赛需要获取你的个人信息，设计一个程序，
    运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
    2、数据存储完了，然后输出个人介绍，格式如下:  
    我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
    3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
    4, 平台为了保护你的隐私，需要你删除你的联系方式；
    5, 你为了取得更好的成绩， 你添加了自己的擅长技能，至少需要 3 项。

二、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，去除重复元素后，统计列表元素个数

"""

# 第一题

# 1、存储个人信息
name = input('请输入姓名：')
gender = input('请输入性别:')
age = input('请输入年龄：')
user_info = dict(name=name, gender=gender, age=age)
print('当前信息如下:',user_info)

# 2、个人介绍
print('我的名字:{}，今年{}岁，性别:{}，喜欢敲代码'.format(name, age,gender))

# 3、添加信息
user_info['height'] = input('请输入身高：')
user_info['phone'] = input('请输入联系方式：')
print('当前信息如下:',user_info)

# 4、删除联系方式
user_info.pop('phone')
print('删除联系方式后信息如下:',user_info)

# 5、添加擅长技能
skill1 = input('请输入擅长技能1:')
skill2 = input('请输入擅长技能2:')
skill3 = input('请输入擅长技能3:')
user_info.update({'skill1': skill1, 'skill2': skill2, 'skill3': skill3})
print('添加技能后信息如下:',user_info)

# 第二题：统计不重复的个数
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li = list(set(li))
print(len(li))


