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
from mylogger import log
from register import register
from read_excle import ReadExcle
from py23_16day.project_V1.ddt import ddt, data

"""
ddt：能够实现数据驱动：通过用例数据，自动生成测试用例
自动遍历用例数据，去生成测试用例，

没遍历出来一条用例的数据，会当成一个参数，传到生成的用例中去


"""

@ddt
class RegisterTestCase(unittest.TestCase):
    excle = ReadExcle("cases.xlsx", 'register')
    cases = excle.read_data_obj()

    @data(*cases)
    def test_register(self, case):

        # 第一步  准备用例数据
        # 获取用例的行号
        row = case.case_id + 1
        # 获取预期结果
        excepted = eval(case.excepted)
        # 获取用例入参
        data = eval(case.data)

        # 第二步： 调用功能函数，获取实际结果
        res = register(*data)

        # 第三步：比对预期结果和实际结果
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            log.info("用例：{}，执行未通过".format(case.title))
            self.excle.write_data(row=row, column=5, value="未通过")
            log.error(e)
            raise e
        else:
            log.info("用例：{}，执行通过".format(case.title))
            self.excle.write_data(row=row, column=5, value="通过")
