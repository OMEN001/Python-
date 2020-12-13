# 单元测试


## unittest
- 测试用例
    - TestCase:使用用例类
    - 测试用例类中test开头的方法就是一个测试用例
- 测试套件
    -  TestSuite:创建测试套件
    - 添加用例到套件的方法：单条 类  模块  目录
- 测试运行程序
    - HTMLTestRunnerNew 创建运行程序，可以生成测试报告
- 测试环境的初始化和恢复
    - setUP:每条用例执行前执行
    - TearDown:每条用例执行之后执行
    
    
## openpyxl

- load_workbook:打开一个工作簿（传入图个excel文件）
- wb[表单名]：选择表单
- 表单对象.cell(row,column)
    
 
    
## ddt 
- ddt
     - 再实测用例类上@ddt

- data
    -测试用例的方法上@data(*ceses) 
    
    
## logging
    - 创建日志收集器对象
    - 设置收集等级
    
    - 创建日志输出渠道：
        - 输出到控制台（设置等级）
        - 输出到文件（设置等级）
        
    - 创建日志输出格式
        - 把输出格式添加到输出渠道上
        
    - 将输出渠道添加到收集器上
        
       





