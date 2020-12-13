"""
============================
Author:柠檬班-木森
Time:2019/10/10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
打开文件：open(文件名，打开的模式（r,a,w），encoding=编码方式)
r模式：读
a模式: 追加写入（在文件内容的结尾处写入）
w模式：写入（覆盖文件中原来的内容）


r模式 打开不存在的文件会报错

a,w模式打开文件，如果文件不存在，则会自动创建一个新的文件

"""


#  如何在python中去打开一个文件

# 打开文件
f = open('data.txt','r',encoding='utf8')


# 文件读取的三种方式

# read():读取文件中所有的内容
# content = f.read()
# print(content)

# readline():读取一行内容
# res = f.readline()
# print(res)

# readlines按行读取所有的内容，每一行的内容当成一个元素，放到一个列表中（最后返回的是一个列表）
# datas = f.readlines()
# print(datas)


# 关闭文件
# f.close()


