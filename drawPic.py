
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')
def add(a,b):
    c = float(a) + float(b)
   # c = a+b
    return c
# 求和
# sum = float(num1) + float(num2)
sum = add(num1 , num2)
 
# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


