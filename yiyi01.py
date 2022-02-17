# encoding: utf-8
"""
@author: duliqi
@contact: dulq@erongdu.com
@time: 2021/12/30 17:57
@file: yuansudingwei.py
@desc: Python
"""

# 基础
# 行连接符
# a = '''abc\
# efg\
# www
# '''
# print(a)

# a = 3
# print(a)
# print(3)
# print(id(a))
# print(id(3))
# print(type(a))
# print(type(3))

# help()
# a = 1
# print(id(1))
# del a  # 删除变量后，并未删除对象
# print(id(1))
# print(id(a))

# x = y = 123
# print(x)
# print(y)

# 系列解包和赋值
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)
# print(a, b, c)

# 变量的互换
# m, n = 10, 20
# print(m, n)
# m, n = n, m
# print(m, n)

# 进制
# print(0b101)  # 二进制
# print(0o666)  # 八进制
# print(0xaa)   # 十六进制

# int()实现类型转换
# a = 10.002
# print(int(a))
# b = True
# print(int(b))
# c = '123'
# print(int(c))
# d = '123.12'
# print(int(d))
# e = '123abc'
# print(int(e))
0
1






















# 自动化项目：需求变更不频繁，项目周期较长，自动化脚本能够重复利用
# 自动化介入点：系统测试阶段
# 实施的过程：可行性分析，框架的选择（selenium，RF），需求分析，自动化率达到多少，计划，用例设计（功能测试里提炼冒烟用例，另外写一套自动化用例，提交报告，脚本维护）


# Python+selenium环境搭建
# Python+pycharm+selenium+Chrome驱动
# 注意：谷歌浏览器的版本与驱动版本要一致



# 元素定位
# 元素定位不到如何解决：
# 原因：1.元素加载没有完成  2.框架frame中   3.元素不可读，不可见，不可用   4.动态属性，动态的DIV层


# 定位前提：需要定位的元素或属性必须唯一
# 定位方式：id, name, css, xpath, link_text, partail_link_text， class_name, tag_name
# 元素定位不到的尽量用css, xpath
#



from selenium import webdriver
# id 定位

