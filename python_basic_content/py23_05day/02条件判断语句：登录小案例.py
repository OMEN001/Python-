"""
============================
Author:柠檬班-木森
Time:2019/9/26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
条件判断：登录小案例

if语法规则:

if  条件比较语句：
    # 条件成立的时候 会执行的代码
else:
    # 条件不成立的时候 会执行的代码
    
    
# 比较预算符  和逻辑运算符（应用场景一般是结合条件判断语句一起使用）


"""
# 定义一个字典，存储一个账号 密码
user = {'uid': "python", "pwd": "123qwe"}

# 第一步：用户输入账号，密码
uid_1 = input('请输入账号：')
pwd_1 = input("请输入密码：")

# 第二步 判断账号密码是否正确
# if uid_1 == user['uid']:
#     print('用户输入的账号是正确的')
#     if pwd_1 == user['pwd']:
#         print("密码正确，登录成功")
#     else:
#         print('您输入的密码有误！')
# else:
#     print("您输入的账号有误！")


# 条件判断中使用逻辑运算符：and  or  not

if uid_1 == user['uid'] and pwd_1 == user['pwd']:
    print("账号密码正确，登录成功")
else:
    print("您输入的账号或者密码有误！")
