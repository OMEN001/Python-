#这道题是注册用户，将注册好的用户写道txt文件中去（注意的是要提前创建好txt然后在里面添加一个列表）
def register():
    try:
        with open('zy_091.txt', 'r', encoding='utf8') as f:
            #读取内容
            data = f.read()
            #因为读取到的内容为字符串，要用eval函数来识别字符串中的列表（）
            users = eval(data)
    except FileNotFoundError:
        users = []
    while True:
        username = input("请输入用户名：")
        for user in users:
            if username ==user["name"]:
                print("该用户已存在！")
                break
        else:
            password = input('请输入密码：')
            password1 = input('请再次确认密码：')
            if password != password1:
                print('注册失败，两次输入的密码不一致')  # 账号和密码不一致 重新输入
                # continue
            else:
                # 账号不存在 密码不重复，则添加到账户列表中
                users.append({'name': username, 'password': password1})
                print('注册成功！')
                break
    with open('zy_091.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串
        content = str(users)
        # 写入文件
        f.write(content)
register()


# import random
# def work3():
#     print('---石头剪刀布游戏开始----')
#     print('请按下面提示出拳：')
#     # 创建一个列表来存储 石头 剪刀 布
#     li = ['石头', '剪刀', '布']
#
#     while True:
#         print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
#         # 用户输入数字
#         try:
#             user_num = int(input('请输入你的选项：'))
#         except ValueError:
#             print('您出拳有误，请按规矩出拳')
#         else:
#             # 电脑随机生成数字
#             r_num = random.randint(1, 3)
#             if 1 <= user_num <= 3:
#                 # 判断用户和电脑是否相等
#                 if r_num == user_num:
#                     print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
#                 # 判断用户胜利的情况
#                 elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
#                     print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
#                 else:
#                     print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
#             # 用户输入4，游戏结束
#             elif user_num == 4:
#                 print('游戏结束')
#                 break
#             else:
#                 print('您出拳有误，请按规矩出拳')
#
# work3()

"""
用户注册问题将注册的用户写入txt文件中的思路：
1.已存在的txt文件(txt文件中要写入列表“[]”)  
  #打开txt文件  with open("xxx.txt","r",encoding='utf8') as f:
  #读取美容     data = f.read()
  #因为读取到的数据格式为字典嵌套在列表中用引号括起来的格式“[{“a”:"a","a":"a"}{“a”:"a","a":"a"}]”
   所以要用eval函数识别字符转中的列表 users = eval(data)
  #执行用户注册操作并将注册的用户已字典的形式添加在列表中 users.append({'name': a, 'password': p})
  #    with open('zy_091.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串
        content = str(users)
        # 写入文件
        f.write(content)
        
2.不存在的txt文件（用异常捕获来解决问题）
  #用try 来执行  with open("xxx.txt","r",encoding='utf8') as f:  读取文件的操作
               data = f.read()
               users（代表的是txt文件中存放用户信息的列表） = eval(data)
  #如没有找到文件用 except FileNotFoundError 处理文件，处理方式为定义一个列表 list = []
  #执行用户注册操作
  #执行用户注册操作并将注册的用户已字典的形式添加在列表中 users.append({'name': a, 'password': p})
  #    with open('zy_091.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串
        content = str(users)
        # 写入文件
        f.write(content)
        
        
3.异常处理
        1、try的作用
            try可以用来监测代码是否出现异常（把有可能出现异常的代码放在try里面）
        2、except下面的代码什么时候执行：
            try中的代码出现异常，被except成功的捕获之后执行，会执行except中的代码。
        3、else下面的代码什么时候执行:
            try中的代码没有出现异常，执行else中的代码
        4、finally下面的代码什么时候执行:
            不管try中的代码是否发生异常，finally下面的代码都会执行
"""