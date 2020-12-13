"""
============================
Author:柠檬班-木森
Time:2019/10/10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random

a = 100


def work():
    print('test01中的work函数')
num = 999
# 魔法变量：__name__:
print('__name__的值：',__name__)

#  模块导入的时候不希望执行的代码
if __name__ == "__main__":
    num = random.random()
    print(num)


