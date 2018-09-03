# -*- coding: utf-8 -*-
import _elementtree as ET
import os
from lxml import etree as etree

# file_path = str(r"C:\workspace\Test\Xml.txt")
# # 定义获取文件行数的方法
# def linecount(filepath):
#     with open(filepath,'r') as f:
#          return len(open(filepath,'r').readlines())

# filelinecount=linecount(file_path)
# print(filelinecount)

# files = open(r"C:\workspace\Test\Xml.txt","r")
# print(files)

# with open(r"C:\workspace\Test\Xml.txt",'r') as f:
#     filelinecount = len(open(r"C:\workspace\Test\Xml.txt",'r').readlines())
#     print(filelinecount)

# with open(r"C:\workspace\Test\Xml.txt",'r') as f:
#     # content = [f.rstrip("\n") for f in f]
#     # print(content)
#     lines_list = f.readlines()
#     print(lines_list)
    # for line in lines_list:
    #     line1 = line[0:]
    # #     print(lines_list)
    #     print(line1)

    # mylines = f.readlines()
    # for myline in mylines:
    # # 逐行查找，如果找到该行第一次有符号“<”,则返回行数给我
    # filesbodysigh = myline.find("<")
    # while filesbodysigh = 0
    #
    #   print(myline)

# file_path = str(r"C:\workspace\Test\Xml.txt")
xslt='''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="no"/>
<xsl:template match="/|comment()|processing-instruction()">
 <xsl:copy>
 <xsl:apply-templates/>
 </xsl:copy>
</xsl:template>
<xsl:template match="*">
 <xsl:element name="{local-name()}">
 <xsl:apply-templates select="@*|node()"/>
 </xsl:element>
</xsl:template>
<xsl:template match="@*">
 <xsl:attribute name="{local-name()}">
 <xsl:value-of select="."/>
 </xsl:attribute>
</xsl:template>
</xsl:stylesheet>
'''
# xslt = str(r"C:\Users\Edward & Bella\Desktop\WorkStaf\Python资料\CSDN-XML\Areo_4.xml")
with open( r'C:\workspace\xlst.xml', 'r' ) as xslt,open( r'C:\workspace\Areo_4.xml', 'r',encoding="utf-8" ) as xml:
    s_xml = etree.parse(xml.read())
    s_xslt = etree.parse(xslt.read())
    transform = etree.XSLT(s_xslt)
    out = transform(s_xml)
    print(out.tostring())