#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from jieba_explicit import *
from special_words import *
from bs4 import BeautifulSoup
from database import *
from datetime import date

# print("中國時報")
# cnt=0
# l=[]
# url="http://www.chinatimes.com/realtimenews?page="
# while cnt<5:
    
#     cnt+=1
#     print(cnt)
#     r=requests.get(url+str(cnt))
#     c=r.content
#     soup=BeautifulSoup(c,"lxml")
#     all_content = soup.find("div",{"class":"listRight"})
#     all_article = all_content.find_all("li",{"class":"clear-fix"})
#     for article in all_article:
#         d={}
#         title = article.find("h2").find("a", href = True).text
#         href = article.find("h2").find("a", href = True).get("href")
#         time = article.find("time").text
#         category = article.find("div",{"class" : "kindOf"}).text
        # print(time)
        # print(category)
        # print(title)
        # print(href)

print(date.today())   