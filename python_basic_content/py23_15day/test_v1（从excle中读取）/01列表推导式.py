
"""
============================
Author:柠檬班-木森
Time:2019/10/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


data = []


for i in range(5):
    data.append('data{}'.format(i))

print(data)

# 列表推导式
data1 = ['data{}'.format(i) for i in range(5)]

print(data1)

data2 = [i for i in range(5)]
print(data2)


data3 = [i for i in range(5,101,5)]
print(data3)


#  创建一个:['line1','line2',line3....lin100]
data5 = ['line{}'.format(i) for i in range(1,101)]


print(data5)


