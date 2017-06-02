#!/usr/bin/env python3

import jieba
import requests
from bs4 import BeautifulSoup

url="http://www.appledaily.com.tw/realtimenews/article/life/20170602/1131569/5測站降雨破500毫米　鄭明典：非颱風的超大豪雨事件"
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

