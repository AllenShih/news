#!/usr/bin/env python3

import jieba
import requests
from bs4 import BeautifulSoup

url="http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132663/【更新】暴雨影響%E3%80%807公路路段今下午仍封閉"
r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,"lxml")

# jieba.set_dictionary('dict.txt.big')

all=soup.find_all("div",{"class":"articulum trans"})

text=all[0].text

# jieba.suggest_freq("土石流", True)
# jieba.suggest_freq("中颱", True)
# jieba.suggest_freq("強颱", True)
# jieba.suggest_freq("全台", True)

# seglist = jieba.cut(text, cut_all=False)

# for item in seglist:
#     if item=="googletag":
#         break
#     print(item)

with open("dict.txt.big") as f:
    content = f.readlines()
    for item in content:
        words = item.split(" ")
        if words[0] in text:
            # print("exist")
            text=text.replace(words[0], " ")
    print(text)



