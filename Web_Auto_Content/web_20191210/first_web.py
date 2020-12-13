#!/usr/bin/python3
"""
@File    : first_web.py
@Time    : 2019/12/10 19:50
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
"""
web自动化： 代码帮你点点点。 -- 非常依赖页面
selenium是什么？1.0   2.0   3.0
一套工具：1）ide录制工具 - 你打开录制，你操作一遍。录下来然后回放。
         2）selenium webdriver - web操作库(访问网页/输入/点击) - 结合代码来实现。
         3）grid(分布式) - 并发/多浏览器(ie/google/firefox)

功能测试：功能/样式  sikuli-图形比对。airTest-游戏测试-图形比对
"""

from selenium import webdriver

# 打开对应的浏览器，开启与浏览器之间的会话。
driver = webdriver.Chrome()  # 接口：newSession # 封装了一系列对网页的操作指令
# 1、启动chromdriver，在线状态。
# 2、python客户端，与chromedriver建立连接。

# api ?? 命令类型？每一个命令-接口-url?请求类型？请求参数？ --- 暗号全称：jsonWireProtocol
# http请求，json格式的数据表达。
# 打开网页  命令名称：get
driver.get("http://www.baidu.com")    # http
# 关闭浏览器 - command -
# driver.quit()



