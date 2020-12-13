"""
============================
Author:柠檬班-木森
Time:2019/10/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import time
import unittest
from register import register


class RegisterTestCase(unittest.TestCase):

    def __init__(self, method_name, case_data):
        self.case_data = case_data
        super().__init__(method_name)

    def test_register(self):
        # 预期结果：
        excepted = eval(self.case_data["excepted"])
        # 参数：data
        #这里加eval的意思是从excle中读取的数据以字符串的方式保存在列表中的
        data = eval(self.case_data['data'])
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        self.assertEqual(excepted, res)
