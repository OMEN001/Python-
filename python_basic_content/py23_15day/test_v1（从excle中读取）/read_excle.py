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

    def read_data_obj(self):
        """读取数据的方法,数据返回的是列表嵌套对象的形式"""
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
        for r in rows[1:]:
            # 每遍历一行，创建一个列表，用例存放该行的数据
            data = []
            # 遍历该列的所有格子
            for c in r:
                # 将每个格子的数据加入到该行的列表中
                data.append(c.value)
            # 将表头和该行的数据进行聚合打包，转换字典
            item = list(zip(title, data))
            # print(item)
            # 创建一个用例数据对象
            case = CaseData()
            for i in item:
                # print(i)
                # 通过反射机制，将表头设为对象属性，对应值设为对象的属性值
                setattr(case,i[0],i[1])
            # print(case)
            # 将该行的用例数据加入到cases这个列表中
            cases.append(case)
        # 将读取好的数据返回出去
        return cases

    def write_data(self):
        """写入数据"""
        pass


if __name__ == '__main__':
    read = ReadExcle('cases.xlsx', 'register')

    data = read.read_data_obj()
    print(data)
