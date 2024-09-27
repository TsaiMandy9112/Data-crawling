#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests, json  # dictionary {}
import matplotlib.pyplot as plt # as是縮寫的意思

url = "https://www.dcard.tw/service/api/v2/forums/dressup/posts?limit=60"


headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
           'cookie': '__auc=fea80fb417c1181b36c5949181d; __gads=ID=4e044326982b3c93:T=1632381286:S=ALNI_MbAYwOrtOm1t6lQf1d7jllGSNEnZA; _sp_id.9717=b37ec8e3-3c0e-429c-a461-fb681f5e62f2.1633683219.1.1633685460.1633683219.9c85c47d-dad5-4e32-a3e8-ef6b85ead111; _fbp=fb.1.1634623298952.1807735667; __htid=36e69cd5-f5b7-48bd-ae2a-716d66ef58b4; cto_bundle=WK5uDl9LYVdsRDFpN0tLNyUyRldxOFpsSEkyb3klMkZQbkhnUEo3Z2RBcUZMZkVKWGFDZjRibzVZUno5bnlWZTBQSGluczJBYlB0a1p5UGlyRUt3aXZoNFdLWjJ0NTNMSlFrSnFUWHBleHRmbGVocE44QnpJeXhDbzJNcm9oSW05TnExQkJSUDBYS3JIWmhMQlVNUGlyUTRWeFNwN0x3JTNEJTNE; _cfuvid=PZ2bE47fOmjruWaMamknUXlUwzhYL820deAeZeiFCU8-1664954647974-0-604800000; _gid=GA1.2.1472264245.1664954649; __gpi=UID=0000051768d370a3:T=1651293745:RT=1664954652:S=ALNI_Mbdd-36MCEyHqmGzTIIvj0C0y4TeA; cf_chl_2=48c0353b279e7ea; cf_chl_prog=x16; cf_clearance=Z.mB1o3.ZjJK4CDCNmvaV9EOOOfYbEP12Q4TIuHGkQ4-1664954880-0-250; _ga_C3J49QFLW7=GS1.1.1664954648.51.1.1664955188.0.0.0; _ga=GA1.1.146392828.1632381285'}
res = requests.get(url, headers = headers)
#透過requests.get()請求上述網址內容，並且將請求結果放入等號左邊的res變數存放。

resjson = json.loads(res.text)
#藉由json.loads()載入上述請求完成的text內容，並將它放入等號左邊的resjson變數存放。

gender_count = {'F':0, 'M':0, 'D':0} 

for outcome in resjson:
    gender_count[outcome['gender']] = gender_count[outcome['gender']]+1
    
figure_name = ['Female', 'Male', "客服小天使"] 

total = [gender_count['F'], gender_count['M'], gender_count['D']]

plt.bar(figure_name, total)

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

#由於pyplot在預設形況下中文資料會出現亂碼，故透過rcParams來設定能夠支援的中文字型。
#若上述['SimHei']無法正常顯示表示電腦內缺乏該字型，此時可改成['DFKai-SB']字型或其他字型來代替。


# In[3]:


res


# In[5]:


res


# In[7]:


gender_count


# In[2]:


res


# In[5]:


res


# In[6]:


resjson


# In[ ]:




