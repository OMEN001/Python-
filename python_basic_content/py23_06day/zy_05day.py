"""
============================
author:MuSen
time:2019/8/1
E-mail:3247119728@qq.com
============================
"""

"""
1、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或
20%）和最终价格。

判断点：
50-100
大于100




2、一个 5 位数，判断它个位与万位相同，十位与千位相
同。 根据判断打印出相关信息。

3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则
印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数


4、使用循环和条件语句完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示 用户胜、负还是平局。运行如下图所示：

# 用户胜利
user       random   
1             2     1
2             3     1 
3             1     -2

# 平局
用户和电脑数一样的

# 电脑胜利：

if random-user ==1 or random-user==-2:
    print(用户胜利)
elif random==user:
    print(平局)
else:
    print(电脑胜利)
    





"""

# 第一题
money = int(input('请输入购买金额:'))
if money < 50:
    print('没有折扣，您需要支付{}元'.format(money))
elif 50 <= money <= 100:
    print('折扣为10%，您需要支付{}元'.format(money - money * 0.1))
else:
    print('折扣为20%，您需要支付{}元'.format(money - money * 0.2))

s = '12321'
    #01234
    #-5,-4,-3,-2,-1
# s[0] == s[4]  s[1] ===s[3]
# 第二题
num_str = input('请输入五位数字:')
if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
    print('此数字符合规范:{}'.format(num_str))
else:
    print('此数字不符合规范')

# 第三题
import random

n = random.randint(1, 9)
my_num = int(input('请输入数字:'))
if n < my_num:
    print('大于随机数')
elif n == my_num:
    print('等于随机数')
else:
    print('小于随机数')

# 第四题

import random

print('---石头剪刀布游戏开始----')
print('请按下面提示出拳：')
# 创建一个列表来存储 石头 剪刀 布
li = ['石头', '剪刀', '布']

while True:
    print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
    # 用户输入数字
    user_num = int(input('请输入你的选项：'))
    # 电脑随机生成数字
    r_num = random.randint(1, 3)
    if 1 <= user_num <= 3:
        # 判断用户和电脑是否相等
        if r_num == user_num:
            print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
        # 判断用户胜利的情况
        elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
            print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
        else:
            print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
    # 用户输入4，游戏结束
    elif user_num == 4:
        print('游戏结束')
        break
    else:
        print('您出拳有误，请按规矩出拳')
