"""
============================
Author:柠檬班-木森
Time:2019/10/12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os

f_path = "C:\project\py23_class\py23_04day\zy_03day.py"

with open(f_path, 'r', encoding='utf8')as f:
    f.read()

# res = os.path.dirname(f_path)
# print(res)

# 魔法变量
# __file__:代表当前文件在电脑中的绝对路径
print(__file__)

# os.path.dirname:获取路径的父级目录
res = os.path.dirname(__file__)
res2 = os.path.dirname(res)
base_dir = os.path.dirname(res2)

f2 = base_dir +'\\'+'py23_04day'+'\\'+'zy_03day.py'
print(f2)

print(base_dir)

# os.path.join: 做路径拼接的
file_path = os.path.join(base_dir,'py23_04day','zy_03day.py')
print(file_path)