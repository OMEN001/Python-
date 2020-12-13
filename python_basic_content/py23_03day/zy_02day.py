"""
============================
author:MuSen
time:2019/7/24
E-mail:3247119728@qq.com
============================
"""
"""
作业
1、用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False
（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法转换为数值类型，再做判段，）

2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间）
，最后计算出应该支付的金额！

3、现在有变量a = ('hello','python','!')
通过相关操作转换成字符串：'hello python !'（注意点:转换之后单词之间有空格）

4、随机生成一个130开头的手机号码

"""
import random

# 第一题：

print('----------第1题----------------')
# 用户输入
num = input('请输入数字:')
# 转换成int  或者float也可以
# num = int(num)
num = float(num)



# 条件预算符做比较，打印结果
print(num % 2 == 0)

print('----------第2题----------------')
# 第二题
# 输入价格
price = input('请输入价格：')
# 转换为浮点数
price = float(price)

# 生成斤数
num = random.randint(5, 10)
print('购买斤数：', num)
# 计算价格
res = price * num
print('支付金额：', res)

print('----------第3题----------------')
# 第三题
a = ('hello', 'python', '!')
# 使用join方法
res = ' '.join(a)
#  repr：显示字符串原始形态
print(res)

print('----------第4题----------------')
# 第四题
r = random.randint(10000000, 99999999)
print(r)
phone = "130" + str(r)
print(phone)
