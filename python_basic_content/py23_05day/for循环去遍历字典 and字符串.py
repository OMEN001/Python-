"""
============================
Author:柠檬班-木森
Time:2019/9/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

dic = {"a": 11, "b": 22, "c": 33}

# 遍历字典的键
# for i in dic:
#     print(i)


# 遍历字典的值
# for i in dic.values():
#     print(i)

# 遍历字典的键值对
for i in dic.items():
    print(i)

for k, v in dic.items():
    print(k)
    print(v)
    print('------------------')

# 元祖拆包
# a, b, c = (11, 22, 33)
# print(a)
# print(b)
# print(c)


print(dic.items())