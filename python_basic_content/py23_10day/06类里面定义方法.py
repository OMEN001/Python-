"""
============================
Author:柠檬班-木森
Time:2019/10/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
定义在类里面的函数：叫做方法（本质上还是函数）

实例方法的第一个参数必须要写成self,这个参数是不需要传参的

"""


class Cat:
    """
    定义一个猫类
    """
    # 类属性

    teg = "四条腿"
    tail = "有尾巴"

    # 定义实例属性通过初始化方法（__init__）来定义
    def __init__(self, age, name):
        # 定义实例属性，
        print(self)
        self.age = age
        self.name = name
        print("正在给对象设置属性")

    def skill1(self):
        print('{}猫的技能1,吃鱼'.format(self.name))

    def skill2(self):
        print('{}猫的行为2:抓老鼠'.format(self.name))


# 创建对象
kt = Cat(age=18, name="凯蒂")
hh = Cat(age=20,name='灰灰')

# 通过对象调用实例方法
kt.skill1()

kt.skill2()

hh.skill1()

hh.skill2()

"""
定义一个测试用例类：


"""




