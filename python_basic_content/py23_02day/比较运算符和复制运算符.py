"""
============================
Author:柠檬班-木森
Time:2019/9/19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
比较运算符：


赋值运算符：



=
+=  
-=
/=
*=


逻辑运算： 
and  :所有的条件都成立，返回True,否则返回False
or   :只要一个以上条件都成立，返回True
not  :去反
.....


成员运算符


身份运算符


"""

a = 10
b = 3

a += 1  # a = a+1
a += 5
a -= 2  # a = a - 2
print(a)

a = (3 + 5) - ((7 * 6) - 20)

res = (8 > 4 or 6 > 7) and (not 8 < 9)
print(res)
