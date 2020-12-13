"""
============================
Author:柠檬班-木森
Time:2019/10/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1、上课的代码全部敲一遍

2、有一组数据，如下格式：
[
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
{'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 5,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'}, 
]
请列表中的每个字典遍历出来，每个字典的数据用一个对象来保存，
要求：使用上次作业的测试用例类的实例对象来保存每个字典中的数据
字典中的key对应属性名，value为属性值。（不使用setattr）
最后把所有的测试用例对象，放入一个列表中，得到如下如格式的数据：
[用例对象，用例对象，用例对象...]



3、定义一个如下的类

class CaseData:
    pass
    
通过setattr(反射机制)将第二题中给的数据 ，保存为第二题要求的格式 


"""


# 第二题
class Cases:
    """用例类"""

    def __init__(self, case_id, url, data, method, excepted, actual):
        self.case_id = case_id
        self.url = url
        self.data = data
        self.method = method
        self.excepted = excepted
        self.actual = actual


data = [
    {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 2, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
    {'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
    {'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'},
    {'case_id': 5, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '通过', 'excepted': '通过'},
]


# 方式一
def work2_1(data):
    new_data = []
    for i in data:
        case = Cases(i['case_id'], i["url"], i['data'], i['method'], i['excepted'], i['actual'])
        new_data.append(case)
    return new_data


# 方式二：
def work2_2(data):
    # 创建一个新列表
    new_data = []
    # 遍历列表
    for i in data:
        # 创建一个对象，将遍历得到的数据传入到类的init方法中，进行初始化（属性设置）
        case = Cases(**i)  # 此处使用**对字典进行解包
        # 将创建出来的对象，放入新列表
        new_data.append(case)
    return new_data


work2_2(data)
res1 = work2_2(data)
print(res1)

# 第三题

class CaseData:

    pass


# 方式一
def work3_1(data):
    # 创建一个新列表
    new_data = []
    # 遍历列表，
    for i in data:   #for循环遍历出列表中的字典
        # 创建一个对象
        case = CaseData()
        # 遍历出当前字典的所有数据
        for k, v in i.items():   #遍历从列表中遍历出的字典的键值对

            setattr(case, k, v)   # 将遍历出来的数据设置为对象的属性
        # 将设置好属性的对象，加入到列表中
        new_data.append(case)
    return new_data
    # print(new_data)


data = work3_1(data)
print(data)
# for case in data:
#     print(case.url)



#  case['url']
#  case.url











# 扩展(非作业：课堂上讲)
class CaseData2:
    def __init__(self, item):
        for k, v in item.items():
            setattr(self, k, v)



def work4(data):
    new_data = []
    for i in data:
        case = CaseData2(i)
        new_data.append(case)
    return new_data
