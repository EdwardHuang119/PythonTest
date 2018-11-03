#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import *

#df1=DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})In[16]:)
df1=DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2=DataFrame({'key':['a','b','d'],'data2':range(3)})
df_12=pd.merge(df1,df2)
# df_12=pd.merge(df1,df2,how='outer')
print(df_12)

# print(df1)
# print(df2)

df3=DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4=DataFrame({'rkey':['a','b','d'],'data2':range(3)})
# print(df3)
# print(df4)
# 很明显看到dr3有c行的数据，df4有d的数据都没有了。这是一个很好的去除重复的方案
# df_34=pd.merge(df3,df4,left_on='lkey',right_on='rkey')
df_34=pd.merge(df3,df4,left_on='lkey',right_on='rkey')
# print(df_34)
# j经过确认原来的dataframe并没有变化，只有对原来的dataframe做处理的时候会有drop与否的操作
# print(df3)
# print(df4)

