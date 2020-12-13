"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
随机数模块 random

"""

import random

# 生成一个0-1之间的浮点数
a = random.random()
print(a)

# 在指定的范围内，随机生成一个整数
b = random.randint(0,3)
print(b)

# 随机生成一个手机号码，130+

number = random.random()
number1=str(number)         #这里就是将number转化为字符串，只有字符串才能够截取
number2 = number1[2:10]
mobilephone = "130" + number2   #这里130不加双引号就是整型与number2的数据类型一直就不能拼接
print(mobilephone)