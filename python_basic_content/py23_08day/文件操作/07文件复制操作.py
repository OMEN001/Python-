"""
============================
Author:柠檬班-木森
Time:2019/10/10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

with open('01文件的打开和关闭.py','r',encoding='utf8') as f:
    c = f.read()


with open('copy01.py','w',encoding='utf8') as fw:
    fw.write(c)

