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
# 在没有行列命名索引的dataframe中这个处理是可以的
# print(frame)
# print(frame['Ohio'])
# 如下代码都执行失败，可见在dataframe这个方案不可行
# print(frame['a'])
# 用如下代码给行和列命名
frame.index.names=['key1','key2']
frame.columns.names=['state','color']
# print(frame)
# print(frame['Ohio'])
# 看看用什么方法直接搜索第二层索引
# print(frame[:,'Green']) #失败的方案
frame_2 = frame.swaplevel('key1','key2')
# print(frame)
# print(frame_2)

# frame_3=frame.sortlevel(1) #针对整个frame进行更改，相当于对key2进行排序
# print(frame_3)

# frame_4=frame.swaplevel(0,1).sortlevel(0)#sortlevel已经有新函数替代了，sort_index
frame_4 = frame.sort_index(0,1)
# frame_4 = frame.sort_index(0,1).sort_index(0)
# print(frame_4)



# frame1=DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':[0,1,2,0,1,2,3]})
# print(frame1)

# ser3=Series(range(3),index=[-5,1,3])
# print(ser3)
# print(ser3[-5])

frame5=DataFrame(np.arange(6).reshape(3,2),index=[2,0,1])
print(frame5)
frame_5 = frame5.iloc(0)
print(frame_5)


