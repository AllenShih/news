#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from database import Database

# from datetime import date

# dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

# database = Database(dbname)

# # database.insert("蘋果日報","title","date+" "+time","category","url")

# l=database.search(title="(151551))")
# print(l)

# dat= "2017 / 06 / 02 12:21"
# print(dat.replace(" / ","-"))

import pandas as pd
from special_words import *
import jieba
import requests
import re
from bs4 import BeautifulSoup
from special_words import *
from operator import itemgetter

# from simpledbf import Dbf5 

# df = pd.read_csv("臺灣省道編號座標.csv")

# print(df['Stake'])

# df2 = pd.read_csv("臺灣地區地名資料_具有地標意義公共設施類20161130.csv")

# print(df2['X'])

# with open("dict.txt.big") as f:
#     content = f.readlines()
#     for item in content:
#         print(item.split(" "))

# with open("zip32_9912.csv") as w:
#     content = w.readlines()
#     for lines in content:
#         print(lines.split(","))

# roads = Special_words().road_mark()

# for item in roads:
#     print(item)

# for i in range(len(roads)):
#     for j in range(len(roads[i])):
#         print(roads[i][j])





# with open("at.txt") as f:
#     content = f.readlines()
#     for lines in content:
#         print()

# sec = Special_words().tw_sector()
# city = Special_words().city_mark()
# highway = Special_words().highway_mark()
# landmark = Special_words().land_mark()
# road = Special_words().road_mark()
# print(city)

# with open("zip32_9912.csv", encoding = 'utf8') as w:
#     content = w.readlines()
#     for lines in content:
#         rows = []
#         split_line = lines.split(",")
#         for i in range(4):
#             rows.append(split_line[i])
#     road.append(rows)


# landmark = pd.read_csv("landmark_all.csv")
# name = landmark["Place_name"]
# print(name)

url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132679/雨勢大%E3%80%80南投、高雄部分地區列淹水一級警戒"
r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,"lxml")
main_article=soup.find_all("div",{"class":"articulum trans"})
text=main_article[0].text
text = text.replace("高雄市", "LLL")
print(text)