"""
============================
Author:柠檬班-木森
Time:2019/10/12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
os模块


"""

import os

# 查看当前的工作路径
print(os.getcwd())
# 切换工作路径到父级目录
os.chdir('..')

print(os.getcwd())

os.chdir('路径处理')

print(os.getcwd())

# 获取当前工作路径下所有的文件和目录
# print(os.listdir())
# os.chdir('../../py23_02day')
# print(os.listdir())
# print(os.listdir('C:\project\py23_class'))

# 创建文件夹
# os.mkdir('python666')

# 删除文件夹
# os.rmdir('python666')

# 判断是否是文件
# res= os.path.isfile('C:\project\py23_class\py23_03day\zy_02day.py')
# print(res)
# 判断是否是目录
res3 = os.path.isdir('C:\project\py23_class\py23_03day')
print(res3)