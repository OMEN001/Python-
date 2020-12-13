"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字符串转义
r:反转义，字符串前面加了r之后，字符串中的内容就不会进行转义  \t（空格）  \n（换行） r（不转义）

"""

# s1 = "python\nhello\tpython\thello\tpython\thello"
# print(s1)

#
s2 = r"python\t666"
print(s2)
print('77',end="")   #print输出语句默认会进行换行把end="\n"改为end=" "就是不换行
print('77')
