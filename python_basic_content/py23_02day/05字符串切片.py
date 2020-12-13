"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字符串切片：[起始位置:终止位置+1]

下标索引取值（取单个值）

"""

desc = "名字MUSEN python"

res = desc[0:2]  # 左闭右开
print(res)

res2 = desc[2:7]
print(res2)

res3 = desc[8:20]
print(res3)

# 下标索引取值（取单个值）
print(desc[2])


# 加步长切片(了解)
# 字符串切片：[起始位置:终止位置+1:步长]
str1 = "a1b2c3d4"  #  "1b 2c 3d 4"
print(str1[1::2])



