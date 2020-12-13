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

# 使用多个except来捕获多种异常类型
# try:
#     print(a+'abc')
# # except 后面可以写异常类型（指定只捕获这个类型的错误）
# except TypeError as e:
#     print('捕获到了类型异常')
#     print(e)
# except NameError:
#     print('捕获变量没有定义的错误')
#
#
# print('python666')


# 方式二：一个except指定捕获多个异常类型
# try:
#     print(a+'abc')
# # except 后面可以写异常类型（指定只捕获这个类型的错误）
# except (TypeError,NameError,KeyError) as e:
#     print('捕获到了类型异常')
#     print(e)


# 捕获所有类型的异常（语法错误除外）

try:
    # f = open('ttt.txt')
    aa = 10000
    # print(b)
    print(aa)
    # print(a+'abc')
# except 后面可以写异常类型（指定只捕获这个类型的错误）
except Exception as e:   #Exception 捕获所有类型的异常
    print('捕获到了类型异常')
    print(e)
else:
    # try里面没有捕获到(发生)异常，那么就会执行else里面的代码
    print('没有捕获带异常')
finally:
    # f.close()
    # try里面的代码不管是是否发生异常都会执行
    print('finally----------------')