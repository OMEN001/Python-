"""
============================
Author:柠檬班-木森
Time:2019/10/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import openpyxl

# 第一步：打开excle文件
workbook = openpyxl.load_workbook("cases.xlsx")

# 第二步：选择工作薄中的某个表单（sheet）
sh = workbook["register"]


# 将表单中的内容，按行获取所有的格子
rows = list(sh.rows)
cases = []
# 获取表头，放到一个列表中
title = []
for c in rows[0]:
    title.append(c.value)

# 获取除表头以外的其他行中的数据
for r in rows[1:]:
    data = []
    for c in r:
        data.append(c.value)
    case_data = dict(zip(title,data))
    cases.append(case_data)

print(cases)