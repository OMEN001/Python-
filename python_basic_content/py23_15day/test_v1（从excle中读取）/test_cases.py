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
from read_excle02 import ReadExcle


class RegisterTestCase(unittest.TestCase):
    excle = ReadExcle("cases.xlsx", 'register')

    def __init__(self, method_name, case_data):
        self.case_data = case_data
        super().__init__(method_name)

    def test_register(self):
        # 获取该条用例在excle中的行
        row = self.case_data.case_id + 1
        # 预期结果：
        # excepted = eval(self.case_data["excepted"])
        excepted = eval(self.case_data.excepted)
        # 参数：data
        # data = eval(self.case_data['data'])
        data = eval(self.case_data.data)
        # 调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            # 用例执行未通过
            self.excle.write_data(row=row, column=4, value="未通过")
            raise e
        else:

            self.excle.write_data(row=row, column=4, value="通过")
