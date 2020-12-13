# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import random

# num = int(input("请输入一个数字："))
# if num % 2 ==0:
#     print(True)
# else:
#     print(False)

# b = random.randint(10000000,99999999)
# a  = '{}{}'.format(130,b)
# c = ''.join(('130',str(b)))
# print(c)

# best_language = "PHP is the best programming language in the world! "
# str = best_language.replace('PHP', 'Python')
# print(str)

# li = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
# num = int(input('请输入数字1-7：'))
# print('今天是{}'.format(li[num-1]))

# li2=[1,2,3,4,5]
# li2.insert(0,0)
# li2.insert(5,66)
# li2.extend([11,22,33])
# li2.sort(reverse=False)
# print(li2)

# li = [1,2,3,4,5,6,7,8,9]
# li1=li[2::3]
# print(li1)

# s = 'python java php'
# print(s[7:11])

# li = [1,2,3,4,5,6,7,8,9]
# li.remove(1)
# li.pop(0)
# print(li)
# del li[3]

# 字典的表达方式
# 方式一
# dic = {"keys1":"values1","keys2":"values2"}
# # 方式二
# dic = dict(key1="values1",key2="values2")

# dic = {"name":"lemon","age":"19","nex":"男"}
# # 获取字典的键
# print(dic.keys())
# # 获取字典的值
# print(list(dic.values()))
# # 获取字典的键值对
# print(list(dic.items()))

#1. 输出10行内容，每行的内容都是“*****”。
# i = 1
# while i >= 1:
#     print('*****')
#     i += 1
#     if i==10:
#         break
# 方法二
# i = 10
# while i <= 10:
#     print('*****')
#     i -= 1
#     if i == 0:
#         break

# 2. 乘法表
# 方法一(长方形)
# for a in range(1,10):
#     for b in range(1,10):
#         print('{}x{}={}\t'.format(a,b,a*b),end='')
#     print('')


# 方法二（左上角）
# for a in range(1,10):
#     for b in range(a,10):
#         print('{}x{}={}\t'.format(a, b, a * b), end='')
#     print('')

# 方法三（左下角）
# for a in range(1,10):
#     for b in range(1,a+1):
#         print('{}x{}={}\t'.format(a, b, a * b), end='')
#     print('')

# 方法三（右上角）
# for a in range(1,10):
#     for b in range(1,a):
#         print("        ",end='')
#     for c in range(a,10):
#          print('{}x{}={}\t'.format(a, c, a * c), end='')
#     print('')

# # 方法四（右下角）
# for a in range(1,10):
#     for b in range(1,10-a):
#         print("        ", end='')
#     for c in range(1,a+1):
#         print('{}x{}={}\t'.format(a, c, a * c), end='')
#     print('')

# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and a!=c:
#                 print(''.join((str(a),str(b),str(c))))


# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成.

# num = int(input('请输入利润：'))
# if  0 <= num < 10:
#     num_1 = num*0.1
#     print('利润提成为：',num_1,'万')
# elif  10 <= num <20:
#     num_1 = (num-10)*0.075 + (10*0.1)
#     print('利润提成为：', num_1, '万')
# elif 20 <= num <40:
#     num_1 = 1.75 + (num-20)*0.05
#     print('利润提成为：', num_1, '万')
# elif 40 <= num <60:
#     num_1 = 2.75+(num-40)*0.03
#     print('利润提成为：', num_1, '万')
# elif 60 <= num <100:
#     num_1 = 3.35 + (num - 60) * 0.015
#     print('利润提成为：', num_1, '万')
# else:
#     num_1 = 3.95 + (num - 60) * 0.001
#     print('利润提成为：', num_1, '万')

#任意三个整数类型，x、y、z 提问：要求把这三个数，按照由小到大的顺序输出
# list = []
# for a in range(1,4):
#     b = int(input('请输入一个整数：'))
#     list.append(b)
# list.sort()
# print(list)

# 求1-100所有偶数的和
# sum = 0
# for a in range(1,101):
#     if a%2 == 0:
#         print(a)
#         sum = sum + a
# print(sum)

# 2、一个 5 位数，判断它个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
# num = input('请输入一个五位数：')
# if num[0] == num[4] and num[1]==num[3]:
#     print(num)
# else:
#     print('请重新输入')

# 4、使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示 用户胜、负还是平局。运行如下图所示：
import random
print('---石头剪刀布游戏开始----')
print('请按下面提示出拳：')
print('石头（1）／剪刀（2）／布（3）/退出（4）')
# 创建一个列表来存储 石头 剪刀 布
li = ['石头', '剪刀', '布']
while True:
    num = int(input('请输入你的选项：'))
    rdm = random.randint(1,3)
    if 1 <= num <= 3:
        if num == rdm:
            print('您的出拳为:{}，电脑出拳:{}，结果为平局'.format(li[num - 1], li[rdm - 1]))
        elif num - rdm == -1 or num - rdm == 2:
            print('您的出拳为:{}，电脑出拳:{}，你赢了'.format(li[num - 1], li[rdm - 1]))
        else:
            print('您的出拳为:{}，电脑出拳:{}，你输了'.format(li[num - 1], li[rdm - 1]))
    elif num == 4:
        print('游戏结束！')
        break
    else:
        print('请输入正确的选项！')



