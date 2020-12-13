"""
============================
Author:柠檬班-木森
Time:2019/9/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
while循环：条件循环
语法规则：

while 条件：
    # 条件成立执行的代码
else:
    # 条件不成立的时候，执行的代码



# 使用在循环体中的关键字
break:终止循环，跳出循环体

continue:中止当前本轮循环，开启下一轮循环




注意点：不要出现死循环（注意终止循环的条件）


"""
i = 0

while i < 100:
    print('hello python')
    i += 1
    print('这是第{}次'.format(i))
    if i == 50:
        # break
        continue
    print('------------{}-------------'.format(i))

else:
    print("i小于100不成立，此时i的值{}".format(i))
