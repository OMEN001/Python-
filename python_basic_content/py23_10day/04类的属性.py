"""
============================
Author:柠檬班-木森
Time:2019/10/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类属性和实例属性：

 

"""


class Cat:
    """
    定义一个猫类
    """
    # 共同的特征（属性）：
    # 直接在类里面定义的遍历叫做类属性:这类事物所有的对象都有这个属性，属性值都是一样的
    teg = "四条腿"
    tail = "有尾巴"


hh = Cat()
dd = Cat()
kt = Cat()

# 定义实例属性
kt.age = 20
hh.age = 18
dd.age = 6
kt.name = "凯蒂猫"
hh.name = "灰灰"
dd.name = "叮当"

# 获取属性值：对象.属性  (不能通过类去获取实例属性)
print(kt.age)
print(hh.age)

# 类属性获取
# 通过对象可以获取类属性
print(kt.tail)
print(hh.tail)
# 通过类也可以获取类属性
print('----------')
print(Cat.tail)



