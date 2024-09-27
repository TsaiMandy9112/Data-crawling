#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
from jsonpath import jsonpath

x = 1

for offset in range(5):  #控制換頁迴圈
    
    url = "https://ecapi.pchome.com.tw/cdn/ecshop/prodapi/v2/region/DJAD/salesrank/0/prod&offset=x&limit=20&fields=Id,Nick,Pic,Price,Discount,isSpec,Name,isCarrier,isSnapUp,isBigCart&_callback=jsonp_prodlist&1587471304315?_callback=jsonp_prodlist"
    url = url.replace('x', str(x))
    res = requests.get(url)
    clean_needed = res.text
    
    clean = clean_needed.replace('try{jsonp_prodlist(','').replace(');}catch(e){if(window.console){console.log(e);}}','')
    Json_Data = json.loads(clean)
    
    if len(Json_Data) == 19:
        for times in range(19):
            book_name = jsonpath(Json_Data[times], '$.Nick')
            book_price = jsonpath(Json_Data[times], '$.Price.P')
            print(book_name + book_price)
    else:
        for times in range(20):
            book_name = jsonpath(Json_Data[times], '$.Nick')
            book_price = jsonpath(Json_Data[times], '$.Price.P')
            print(book_name + book_price)
    
    x += 20   # 等同於 x = x + 20


# In[ ]:




