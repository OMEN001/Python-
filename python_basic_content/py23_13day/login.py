"""
============================
Author:柠檬班-木森
Time:2019/10/22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


def login_check(username, password):
    """
    登录校验的函数
    :param username: 账号
    :param password:  密码
    :return: dict type
    """
    if 6 <= len(password) <= 18:
        if username == 'python23' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "mgs": "密码长度在6-18位之间"}


# #  第一步 调用功能函数，传入参数
# result = login_check('python23', 'lemonban')
#
# excepted = {"code": 0, "msg": "登录成功"}
#
# #  第二步  比对预期结果，和实际结果是否一致
#
# if result == excepted:
#     print('用例执行通过')
# else:
#     print('用例执行未通过')

