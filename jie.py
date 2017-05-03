#!/usr/bin/env python3

import jieba
import requests
from bs4 import BeautifulSoup

url="http://www.appledaily.com.tw/realtimenews/article/new/20150927/700101/"
r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,"lxml")

jieba.set_dictionary('dict.txt.big')

all=soup.find_all("div",{"class":"articulum trans"})

text=all[0].text

jieba.suggest_freq("土石流", True)
jieba.suggest_freq("中颱", True)
jieba.suggest_freq("強颱", True)
jieba.suggest_freq("全台", True)

seglist = jieba.cut(text, cut_all=False)

for item in seglist:
    if item=="googletag":
        break
    print(item)

