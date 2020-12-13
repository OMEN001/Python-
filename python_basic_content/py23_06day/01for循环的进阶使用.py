"""
============================
Author:柠檬班-木森
Time:2019/9/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
for循环

break：终止循环

"""

# li = [11, 22, 33, 44, 55]
# #
# for i in li:
#     print(i)
#     if i == 22:
#         continue
#     print('---------1------------')
# else:
#     print("遍历完了")

# 列表中保存的时用户信息

users = [{"name": "py01", "pwd": "123"},
         {"name": "py02", "pwd": "123"},
         {"name": "py03", "pwd": "123"},
         {"name": "py04", "pwd": "123"}]
# # 查找‘py03’这个用户是否存在，
#
#
#


for user in users:
    if user['name']=='py03':
        print("找到了py03这个用户")
        break

else:
    print("没有找到py03这个用户")
