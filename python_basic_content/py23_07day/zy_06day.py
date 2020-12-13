"""
============================
Author:柠檬班-木森
Time:2019/10/7
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 第一题
def mul_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {:<4}'.format(j, i, i * j), end='')
        print()

mul_table()


# 第二题
def count_num():
    count = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and c != b and a != c:
                    print(a, b, c)
                    count += 1
    print('一共有{}个'.format(count))

count_num()
# 第三题
def compute_number():
    print('欢迎使用计算器')
    a = int(input('请输入数字1:'))
    b = int(input('请输入数字2:'))
    print('功能提示:【1】加 【2】减【3】乘 【4】除')
    num = input('请选择：')
    if num == '1':
        return a + b
    elif num == '2':
        return a - b
    elif num == '3':
        return a * b
    elif num == '4':
        return a / b
    else:
        print('没有此选项！')
# res = compute_number()
# print(res)
# 第四题

users = [{'user': 'python23', 'password': 'lemonban'}]
def register():
    # 注册功能
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
register()