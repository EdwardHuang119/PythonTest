#!/usr/bin/envpython
#-*-coding:utf-8-*-
import pandas as pd
import numpy as np
from pandas import *

# data=Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]]）
# print(data)

# print(data['b'])
# print(data.ix[['b','d']])
# print(data[:,2])
# print(data.unstack())
# print(data.unstack().stack())

# 行和列都有索引的dataframe
frame=DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
# 行有索引但是列没有
# frame=DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],columns=['Ohio','Ohio','Colorado'])
# 在没有行列命名索引的dataframe中这个处理是剋的
print(frame)
print(frame['Ohio'])
# 如下代码都执行失败，可见在dataframe这个方案不可行
# print(frame['a'])
# 用如下代码给行和列命名
frame.index.names=['key1','key2']
frame.columns.names=['state','color']
print(frame)
print(frame['Ohio'])
# 看看用什么方法直接搜索第二层索引
# print(frame[:,'Green'])



