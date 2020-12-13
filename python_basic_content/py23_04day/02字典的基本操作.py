"""
============================
Author:柠檬班-木森
Time:2019/9/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 列表
# student = [['MUSNE', 18, '男'],
#            [18, '男', '小明'],
#            [18, '男', '小明'],
#            [18, '男', '小明'],
#            [18, '男', '小明'],
#            ]
#
# s = student[0]
# s2 = student[1]

# 字典的定义：{}
# 字典中的每一条数据数据由两部分组成：key:value（键值对）
# s11 = {"name": "小明", "age": 18, "gender": "男"}
#
# print(s11['name'])


stus = [
    {"name": "小明", "age": 18, "gender": "男"},
    {"age": 18, "name": "小花", "gender": "男"},
    {"age": 18, "gender": "男", "name": "小里"},
    {"age": 18, "name": "小六", "gender": "男"},
]

s0 = stus[0]
s1 = stus[1]
print(s0['name'])
print(s1['name'])

#  测试用例的数据：  接口地址：url   入参：data    预期结果:excepted


case = {'url':'http://www.baidu.com',"data":123,"excepted":111}


# 100条测试用例数据如何存储？
#   列表嵌套字典
