#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import webbrowser
# c = webbrowser.open('http://weibo.com')

# 通过一个dict来录入股票和股票代码的关系并打印出来
# d = {'工商银行': '601398', '中国银行': '601988', '平安银行': '000001'}
# stockname = input('请输入股票的名称：')
# shocknumber = input('请输入股票的代码:')
# d[stockname]=shocknumber
# print(d)
# print(d['工商银行'])
# print(d[stockname])
# 变量在[]中可以不加入引号了。这个比较好。

import tushare
print(tushare.__version__)
c=tushare.get_k_data('601398','2018-05-01','2018-06-01',                z
print(c)