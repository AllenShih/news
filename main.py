#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"

import appledaily
import requests
from bs4 import BeautifulSoup
import csv
import pandas
import time

key_words=["水災","降雨","土石","水量","淹水"]
url="http://www.appledaily.com.tw/realtimenews/section/new/"
apple=appledaily.craw(key_words,url)

print(appledaily)


# cnt=0

# l=[]
# while cnt<500:
#     cnt+=1
#     print(cnt)
#     r=requests.get(url+str(cnt))
#     c=r.content
#     soup=BeautifulSoup(c,"lxml")

#     all=soup.find_all("div",{"class":"abdominis rlby clearmen"})

#     hr="http://www.appledaily.com.tw/"

#     for article in all:
#         date_all=article.find_all("h1",{"class":"dddd"})
#         news_all=article.find_all("ul",{"class":"rtddd slvl"})
#         for i in range(len(news_all)):
#             date=date_all[i].text
#             life_news=news_all[i].find_all("li",{"class":"rtddt life"})+ \
#             news_all[i].find_all("li",{"class":"rtddt life even"})+news_all[i].find_all("li",{"class":"rtddt life even hsv"})
#             for lines in life_news:
#                 d={}
#                 href_back=lines.find('a').get('href')
#                 href=hr+href_back
#                 time=lines.find_next('time').text
#                 category=lines.find_next('h2').text
#                 title=lines.find_next('h1').text

#                 word_cnt=0
#                 for words in key_words:
#                     if words in title:
#                         word_cnt+=1
#                 if word_cnt>0:
#                     d["Time"]=date+" "+time
#                     d["Category"]=category
#                     d["Title"]=title
#                     d["URL"]=href
#                     l.append(d)
#     # if cnt%100==0:
#     #     time.sleep(600)

# df=pandas.DataFrame(l)
# df.to_csv("output.csv")
