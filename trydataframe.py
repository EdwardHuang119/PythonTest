#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame,Series
import numpy as np

data=DataFrame(np.arange(16).reshape((4,4)),
               index=['Ohio','Colorado','Utah','NewYork'],
               columns=['one','two','three','four'])
print(data)
# print(data.index)
# print(data.columns)

# 尝试各种切片赋值方法
# 通过列名称或者列的列表选择全部的行
# print(data['two'])
# print(data[['three','one']])
# 通过数字索引来获取,按照行索引就是切片了全部行的数据
# print(data[:2])
# 通过某列的值的条件来获取对应的行
print(data[data['three']>5])


