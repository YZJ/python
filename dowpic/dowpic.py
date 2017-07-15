# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:46:18 2017

@author: Yangzj
"""

import requests
import re
import os
import time
#page = 1
i=0



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }



def getHTML(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "请求网站链接异常"
        
if __name__  == "__main__":
    
    t=str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    imgPath="C:\\img\\" + t
    print(imgPath)
    os.mkdir(imgPath)
    
    if not os.path.isdir(imgPath):
        print('sb')
        os.mkdir(imgPath)
    
    index=1
    
    url = 'http://www.141545.net/rt-13850-1-1.html'
    html = getHTML(url)
    
    pattern = re.compile('file="(.*?.jpg)"',re.S)
    imgurls = re.findall(pattern, html)
    
    for imgurl in imgurls:
       try: 
           res = requests.get(imgurl,headers = headers)
       except:
           print('未下载成功：',imgurl)
           continue
       print(imgurl)
       filename = os.path.join(imgPath, str(index)+'.jpg')
       with open(filename, 'ab+') as f:
           f.write(res.content)
           print('下载完成\n')
           index += 1
    
        
