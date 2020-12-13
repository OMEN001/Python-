"""
============================
Author:柠檬班-木森
Time:2019/10/11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 第一题
# def work1():
#     # 第一步：读取数据,每一行作为一个元素放到列表中
#     with open('data.txt', encoding='utf8') as f:
#         datas = f.readlines()
#         # print(datas)
#     # 第二步：将数据转换为字典
#     dic = {}
#     # 通过enumerate去获取列表中的数据和下标
#     for index, data in enumerate(datas):
#         # print(index,data)
#         # 构造数据的key和value
#         key = 'data{}'.format(index)
#         # print(key)
#         value = data.replace('\n', '')
#         # print(key,value)
#         # 加入到字典中
#         dic[key] = value
#     return dic
#
#
# # res = work1()
# # print(res)
#
#
# # 第二题
# # 要求一：
# def work2_1():
#     # 第一步：读取数据,每一行作为一个元素放到列表中
#     with open('cases.txt', 'r') as f:
#         datas = f.readlines()
#
#     # 第二步：将数据转换为列表
#     # 创建一个空列表
#     cases = []
#     # 遍历出来每一行数据
#     for i in datas:
#
#         # 将该行数据使用split按，进行分割,得到一个列表
#         itme = i.split(',')
#         # print(itme)
#         # 创建一个空字典，用例存放该行数据
#         dic = {}
#         # 遍历分割后的列表，
#         for j in itme:
#             # 将遍历出来的数据，按:分割，得到key,value,然后加入到字典中
#             key = j.split(':')[0]
#             value = j.split(':')[1].replace('\n','')
#             dic[key] = value
#         # 将该行数据加入到列表中
#
#         cases.append(dic)
#     # 完成转换之后，将转换后的数据 进行返回
#     return cases
#
#
# data2 = work2_1()
#
# # 要求二：
# def work2_2(datas):
#     # 创建一个空字典，用例存放数据
#     dic = {}
#     # 通过enumerate去获取列表中的数据和下标
#     for index, data in enumerate(datas):
#         # 构造数据的key
#         # print(index,data)
#         key = 'data{}'.format(index + 1)
#         # 加入到字典中
#         dic[key] = data
#     # 将转换之后的数据进行返回
#     return dic
# work2_2(data2)


# res = map(lambda x:{'data{}'.format(x[0]+1):x[1]},enumerate(data2))
# print(list(res))
# 第三题
"""
注意点：
我这边数据存储的格式为[{},{}...] ，需要先创建一个users.txt文件并写入一个空列表：[]，
如果没有创建users.txt文件会报错，请先创建一个users.txt文件，写入以下内容
数据为一个空列表，下如：
[]
"""

def work3():
    # 读取文件中注册用户的数据
    with open('users.txt', 'r', encoding='utf8') as f:
        # 读取内容
        data = f.read()
        # 识别字符串中的列表
        users = eval(data)
    # 注册功能代码（上次作业写的，不需要改动）
    while True:
        username = input('请输入新账号:')  # 输入账号
        for user in users:  # 遍历出所有账号，判断账号是否存在
            if username == user['user']:
                print('该账户已存在')  # 账号存在，重新输入
                break
        else:
            password1 = input('请输入密码：')  # 输入密码
            password2 = input('请再次确认密码：')  # 再次确认密码
            if password1 != password2:
                print('注册失败，两次输入的密码不一致')  # 账号和密码不一致 重新输入
                # continue
            else:
                # 账号不存在 密码不重复，则添加到账户列表中
                users.append({'user': username, 'password': password2})
                print('注册成功！')
                break
    # 程序运行结束后，将所有用户的数据写入文件
    with open('users.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串
        content = str(users)
        # 写入文件
        f.write(content)
work3()

# 第四题
# 模块导入
# 方式一： import 模块名
# 方式二： from 模块名 import 模块中的变量或者函数

# 包导入
# 方式一： from 包名 import 模块名
# 方式二： from 包名.模块名 import 模块中的变量或者函数
