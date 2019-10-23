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
# inner就是两者并列集的笛卡尔乘积，outer就是两者合集的
# print(df_12)

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

#有时候，DataFrame中的连接键位于其索引中。在这种情况下，你可以传入left_index=True或right_index=True（或两个都传）以说明索引应该被用作连接键：
# left1=DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
# right1=DataFrame({'group_val':[3.5,7]},index=['a','b'])
# print(left1)
# print(right1)
# leftright = pd.merge(left1,right1,left_on='key',right_index=True)
# # leftright = pd.merge(left1,right1,left_on='key',left_index=True)
# print(leftright)

#对于层次化索引的数据，事情就有点复杂了：
lefth=DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],'key2':[2000,2001,2002,2001,2002],'data':np.arange(5.)})
righth=DataFrame(np.arange(12).reshape((6,2)),index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],[2001,2000,2000,2000,2001,2002]],columns=['event1','event2'])
print(lefth)
print(righth)
# print(pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True))

print(pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='outer'))



#要根据多个键进行合并，传入一个由列名组成的列表即可：
# left=DataFrame({'key1':['foo','foo','bar'],'key2':['one','two','one'],'lval':[1,2,3]})
# right=DataFrame({'key1':['foo','foo','bar','bar'],'key2':['one','one','one','two'],'rval':[4,5,6,7]})
# print(left)
# print(right)
# print(pd.merge(left,right,on=['key1','key2'],how='outer'))

#
