"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import decimal

a = 2.3
b = 2.1
print(a - b)
# 通过decimal  解决浮点数运算的精度问题
a1 = decimal.Decimal('2.3')
b1 = decimal.Decimal('2.1')

print(a1 - b1)
print(type(a1))

# b2 = 2.45
# b3 = 1.56
# print(b2-b3)
# d1 = decimal.Decimal("2.45")
# d2 = decimal.Decimal("1.56")
# print(d1-d2)
# print(type(d1))
