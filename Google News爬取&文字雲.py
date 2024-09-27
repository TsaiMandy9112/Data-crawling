#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests 
from bs4 import BeautifulSoup
import pandas as pd #處理表格型態資料

url = 'https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser') 

titles = soup.select('.ipQwMb.ekueJc.RD0gLb')
links = soup.select('.VDXfz')

news_title = []
news_link = []

for each_title in titles:
    news_title.append(each_title.text)

for each_link in links:
    news_link.append("https://news.google.com" + 
                     each_link['href'].strip('.'))

    
df = pd.DataFrame(  #表格資料，資料框架
{
    '標題': news_title,
    '內容連結': news_link
})
 
df


# In[3]:


cleaned = []

for article_url in news_link:
    res2 = requests.get(article_url)
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    temp_content = soup2.find_all('p')  # select() p = paragraph段落
    for data in temp_content:
        cleaned.append(data.text)


# In[4]:


articleAll = '\n'.join(cleaned)


# In[5]:


articleAll


# In[6]:


articleAll.replace("\n", '').replace('\n\n\n\n', '').replace('\r', '')


# In[8]:


get_ipython().run_line_magic('pip', 'install jieba')


# In[7]:


import jieba #結吧
jieba.load_userdict('dict.txt.big')


# In[8]:


Sentence = jieba.cut(articleAll, cut_all=True)
print('全模式'+": "  + "/ ".join(Sentence) + '\n')  #把句子中所有可以成詞的詞語都掃描出來，速度非常快，但是不能解決歧義。

# test_list = ['A', 'B', 'C']
# print('-'.join(test_list)) # A-B-C

Sentence = jieba.cut(articleAll, cut_all=False)
print('精確模式'+": " + "/ ".join(Sentence)+ '\n')  #試圖將句子最精確地切開，適合文本分析。
 
Sentence = jieba.cut_for_search(articleAll)  
print('搜索引擎模式'+": " + "/ ".join(Sentence)+ '\n') #在精確模式的基礎上，對長詞再次切分，提高召回率，適合用於搜尋引擎分詞。


# In[40]:


Sentence = jieba.cut(articleAll, cut_all=True)
print('全模式'+": "  + "/ ".join(Sentence) + '\n')


# In[41]:


Sentence = jieba.cut(articleAll, cut_all=False)
print('精確模式'+": " + "/ ".join(Sentence)+ '\n')


# In[50]:


Sentence = jieba.cut_for_search(articleAll)  
print('搜索引擎模式'+": " + "/ ".join(Sentence)+ '\n')


# In[12]:


get_ipython().run_line_magic('pip', 'install wordcloud')


# In[9]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud

stopwords = {}.fromkeys(['也', '日', '月', '人', '在', '是', '的', '4', '5', '，', '、', ',', '!', '2', '3',
                        '2021', '12', '22', '「', '」', '(', ')', '！', '（', '）', '。', '/', '／', '?'])


# In[43]:


stopwords  #Key鍵, Value值


# In[51]:


hash


# In[10]:


# 使用cut_for_search(搜尋引擎)斷詞模式並產生字詞頻率的dictionary (並剔除stopwords的計算)
Sentence = jieba.cut_for_search(articleAll)

hash = {}

for item in Sentence:
 
    if item in stopwords: #將不要的字詞排除在雲之外
        continue
    
    if item in hash:
        hash[item] += 1   # hash[item] = hash[item] + 1
    else:
        hash[item] = 1

 
# 文字雲樣式設定


wc = WordCloud(font_path="TW-Kai-98_1.ttf", #設置字體
               background_color="white", #背景顏色
               max_words = 2000,        #文字雲顯示最大詞數
               stopwords=stopwords)      #停用字詞
 
# 使用dictionary的內容產生文字雲
wc.generate_from_frequencies(hash)
 
# 視覺化呈現
plt.imshow(wc)
plt.axis("off")
plt.figure(figsize=(50, 50), dpi = 300)

wc.to_file('output.jpg')


# In[ ]:




