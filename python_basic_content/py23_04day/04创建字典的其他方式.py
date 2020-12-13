"""
============================
Author:柠檬班-木森
Time:2019/9/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 方式一(掌握)
dic1 = {'name': "小明", "age": 18, "gender": "男"}

# 方式二（掌握）
dic2 = dict(name="小明",
            age=18,
            gender="男")


# 方式三：(了解)
#  [('aa', 11)]
dic3  = dict([('aa',11),('bb',234)])


print(dic1)
print(dic2)
print(dic3)


# 合并两个字典的方法：update

dic3.update({"aa":111,"dd":99})
print(dic3)




