#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import re
import os
import linecache

# 写一个文件试试,
# file = open(r'/Users/Mac/Documents/openflie.txt',"w")
# file.writelines('{AAA1111}'+'\n')
# file.writelines('{bbbbb222}'+'\n')
# file.writelines('{ccccc22}'+'\n')
# file.writelines('<ccccc22>'+'\n')
# file.writelines('<ddddd44>'+'\n')
# file.writelines('<eeeee77>'+'\n')
# file.writelines('<zzzz99>'+'\n')
# file.writelines('{ccccc22}'+'\n')
# file.closed

filename = str(r'/Users/Mac/Documents/openflie.txt')
# with open(filename,"r") as f:
#     message_head = f.readline()
#     a = message_head[0:1]
# print(a)

# with open(filename,"r") as f:
#     allmessage = f.read()
#     paint1=allmessage.find("<")
#     paint2=allmessage.find("}")
#     print(paint1,paint2)
#     message_head=allmessage[0:paint2]
#     message_body=allmessage[paint1]
# print(message_head,message_body)

# 尝试分离并获取报文头和报文体，并做基本的检查
# f = open(filename,"r")
# allmessage = f.read()
# paint1=allmessage.find("<")
# paint2=allmessage.find("}")
# print(paint1,paint2)
# message_head=allmessage[0:paint2+1]
# message_body=allmessage[paint1:]
# f.close()
# # print('报文头是：',message_head)
# # print('报文体是：',message_body)

# 尝试一下变成某个函数
def Message_read(filename):
    f = open(filename, "r")
    allmessage = f.read()
    paint1 = allmessage.find("<")
    paint2 = allmessage.find("}")
            # print(paint1, paint2)
    head = allmessage[0:paint2 + 1]
    body = allmessage[paint1:]
    f.close()
    return (head,body)

# def Message_head_read(Message_head)

Message = Message_read(filename)
Message_head = Message[0]
Message_body = Message[1]

# 尝试解析报文头
# if Message_head[0:1] !='{' or Message_head[-1] !='}' :
#     print('包头不符合规范')
# else:
#     Sendbank_head = Message_head[3:14]
#     Recvbank_head = Message_head[16:28]
#     Date = Message_head[28:38]
#     print(Sendbank_head,Recvbank_head,Date)

def Message_head_read(Message_head):
    if Message_head[0:1] != '{' or Message_head[-1] != '}':
        print('包头不符合规范')
    else:
        Sendbank_head = Message_head[3:14]
        Recvbank_head = Message_head[16:28]
        Date = Message_head[28:38]
    return (Sendbank_head,Recvbank_head,Date)

Message_head_read=Message_head_read(Message_head)
print("发报行是:",Message_head_read[0])
print("收报行是:",Message_head_read[1])


# with open(filename,"r") as f:
#     for message_head in f.readlines()[0]:
#         # c = len(message_head)
#         # c = len(message_head)
#         c = message_head[message_head.find('{'):message_head.find('}')]
#         print(c)



# message_head = []
# message_body = []
# with open(filename,"r") as f:
#     if os.path.isfile(filename):  # 判断文件是否存在
#         lines_list = f.readlines()  # 读取文件内容
#         for line in lines_list[1:]:  # 循环读取每一行，1：是从第二行开始
#             message_head.append(line.strip('\n').split('}')[0])  # 截取逗号之前的数据
#             message_body.append(line.strip('\n').split('<')[0])  # 截取逗号之后的数据，分行追加到数组里
#     else:
#         print("Account file does not exist!")
#         sys.exit(0)
# print(message_head)

#     # linecount = len(f.readlines())
#     mlines = f.readline()
#     for mline in mlines:
#         print(mline)
# #   # 这时候打印可以打印出完成可以换行的文件
#     print(message,linecount)
  # 获取文件的行数
# linecount = len(open(filename,'rU').readlines())
#   linecount = len(Mfile.readlines())
#   print(linecount)
def linecount_1(filename):
    return len(open(filename,'r').readlines())  # 最直接的方法
b = linecount_1(filename)
print(b)







# print(linecount)
# m_linelist = Mfile.readline()
# for line in m_linelist:
#     print(m_linelist,line)
#
#   # print(message)
# r2 = linecache.getline('/Users/Mac/Documents/openflie.txt',3)
# print(r2)


# file = open(r'/Users/Mac/Documents/openflie.rtf').read()
# print(file)