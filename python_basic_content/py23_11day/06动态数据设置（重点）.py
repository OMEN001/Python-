"""
============================
Author:柠檬班-木森
Time:2019/10/17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
属性动态设置
反射机制
设置属性：setattr()
获取属性：getattr()+
删除属性：delattr()


"""


class Cases:

    def __init__(self, name):
        self.name = name


case1 = Cases('1111')

# 对象.属性名 =  属性值

datas = {'case_id': 1, "data": '999', "url": "www.baidu.com"}
# 给对象动态设置属性：参数（对象，属性名，属性值）
setattr(case1,'age',99)  #  ==》case1.age = 99
#
print(case1.age)

for k, v in datas.items():
    print(k, v, type(k), type(v))
    # case1.k = v
    setattr(case1, k, v)

print(case1.url)
# # # 删除属性
# delattr(case1,'name')
#
#
#
# # 获取属性值
# res = getattr(case1,'name')
# print(res)



"""
万物皆对象

函数：函数对象
基本的数据：
类：类对象
类创建出来的对象：
模块：模块对象
包：包对象




"""