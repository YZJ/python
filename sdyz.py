# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:02:47 2017

@author: Yangzj
"""

import requests
from bs4 import BeautifulSoup
import traceback
import re
import os

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def main():
    hreflst =[  'http://www.sdyz.cn/zsks/gkxx/2010/07/16/739.html',
             'http://www.sdyz.cn/zsks/gkxx/2011/07/15/995.html',
             'http://www.sdyz.cn/zsks/gkxx/2012/07/17/1191.html',
             'http://www.sdyz.cn/zsks/gkxx/2013/07/18/1390.html',
             'http://www.sdyz.cn/zsks/gkxx/2014/07/16/4301.html',
             'http://www.sdyz.cn/zsks/gkxx/2015/07/18/4710.html',
             'http://www.sdyz.cn/zsks/gkxx/2016/07/11/4882.html']
    

    index = 0
    yearlst=[]
    for href in hreflst:
        pattern = r'\d{4}'
  
        match = re.search(pattern,href).group()

        yearlst.append(match)

    list = []

    for href in hreflst:
        print(href)
        html = getHTMLText(href)
        soup = BeautifulSoup(html, 'html.parser') 
        a = soup.find_all('tr')
          
        filePath="C:\\sdyz\\"
        
        filePath +=  str(yearlst[index])
        if not os.path.isdir(filePath):
            #print('sb')
            os.makedirs(filePath)
        filePath +=  '\\gkinfo.txt' 
        print(filePath)
        
        for i in a:
            for j in range(0,5):
                b = i.find_all('td')[j].string
                list.append(b)
                #list.append('\n')
            with open(filePath, 'a+', encoding = 'utf-8') as f:
                f.write(str(list)+'\n')
                f.close()
            #print(':',len(list))
            list = []    

        index += 1
        filePath = ''
    #    print('----------------------------')
        

 
main()
