from web_20191228.TestDatas.Common_Datas import home_url

# 正常场景 - 测试数据
success_data = {"username": "18684720553",
                "passwd": "python",
                "check_url": home_url}


# 异常场景 - 测试数据 - 手机号码格式/手机号为空/密码为空
wrong_datas = [
    {"username": "", "passwd": "python", "check": "请输入手机号"},
    {"username": "18684720553", "passwd": "", "check": "请输入密码"},
    {"username": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
]

# 异常场景 - 测试数据 - 密码错误/手机号码从未注册
