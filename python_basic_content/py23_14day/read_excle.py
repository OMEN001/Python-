"""
============================
Author:柠檬班-木森
Time:2019/10/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import openpyxl

class CaseData:
    pass


class ReadExcle(object):

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open(self):
        """打开工作表和表单"""
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        """读取数据的方法"""
        # 打开工作簿和表单
        self.open()
        # 将表单中的内容，按行获取所有的格子
        rows = list(self.sh.rows)
        # 创建一个空列表，用例存放所有的用例数据
        cases = []
        # 获取表头，放到一个列表中
        title = []
        for c in rows[0]:
            title.append(c.value)

        # 获取除表头以外的其他行中的数据
    #data = []   如果放在这里的话他会每遍历一行产生一个列表，如[{}],[{},{}],[{},{},{}] 会是这个样子
        for r in rows[1:]:
            # 每遍历一行，创建一个列表，用例存放该行的数据
            data = []
            # 遍历该列的所有格子
            for c in r:
                # 将每个格子的数据加入到该行的列表中
                data.append(c.value)
            # 将表头和该行的数据进行聚合打包，转换字典
            case_data = dict(zip(title, data))

            # 将该行的用例数据加入到cases这个列表中
            cases.append(case_data)
        # 将读取好的数据返回出去
        return cases

    def write_data(self):
        """写入数据"""
        pass

#仅在这个模块中执行以下操作
# if __name__ == '__main__':
#     read = ReadExcle('cases.xlsx','register')
#
#     data = read.read_data()
#     print(data)