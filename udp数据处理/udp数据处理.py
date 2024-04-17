# -*- coding: utf-8 -*-
import re
f2=open('D:/hlht/yuzt/python/pythonScripts/udp数据处理/上海卡-上海天翼云udp延时-20221205-已处理.log','w') 
#f=open('D:\hlht\yuzt\python\pythonScripts\udp数据处理\上海卡-上海天翼云udp延时-20221205.log','r+')
with open('D:/hlht/yuzt/python/pythonScripts/udp数据处理/上海卡-上海天翼云udp延时-20221205.log','r+') as f:
    for line in f.readlines():
        b=re.sub('.*->','',line)
        
        c=re.sub(' ms','',b)
        print(c)
        
        f2.write(c)

f.close()
f2.close()

#.*->


