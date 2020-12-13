"""
============================
Author:柠檬班-木森
Time:2019/10/12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
异常捕获
try:
except:
else:
finally:


"""

a = 100

# print(b)

# try:
#     print(a+'abc')
# except:
#     print('捕获到了异常')
#
# print('python666')


try:
    # 把不确定会不会报错的代码，方法try里面
    with open('ttt.txt','r') as f:
        f.read()
except:
    # 捕获到了异常
    print('打开的文件不存在')
    with open('ttt.txt','w') as f:
        pass