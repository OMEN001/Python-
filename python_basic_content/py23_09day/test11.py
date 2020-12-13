"""
============================
Author:柠檬班-木森
Time:2019/10/12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
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