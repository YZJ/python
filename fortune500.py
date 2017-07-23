# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 20:50:26 2017

@author: Yangzj
"""

import requests
from bs4 import BeautifulSoup
import re
import pymysql
#import MySQLdb

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def insert(s):
    conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd='root',db='test',charset='utf8')
    cursor = conn.cursor()
    for tu in s:
        print(tu[3])
        db3 = tranferStr(tu[3])
        
        print(db3)
        db4 = tranferStr(tu[4])
        sql = 'insert into fortune500 values({},\'{}\',\'{}\',{},{},\'{}\')'.format(tu[0],tu[1],tu[2],db3,db4,tu[5])
        print(sql)
        try:
            cursor.execute(sql)   
        except:
            continue
    conn.commit()
    conn.close()
    

# 转换格式 23,456,789 -> 23456789
def tranferStr(str):
    number = str.replace(',','')
    return number
    
def main():
    href = 'http://www.fortunechina.com/fortune500/c/2017-07/20/content_286785.htm'
    
    html = getHTMLText(href)

    s =re.findall('<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?_blank">(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',html)

    insert(s)

main()