#!/usr/bin/env python3
# -*- coding: utf8 -*-


import requests
from bs4 import BeautifulSoup

# res = requests.get("https://news.google.com")
# soup = BeautifulSoup(res.content,"lxml")
# # print (soup.select(".esc-body"))
# count = 1

# for item in soup.select(".esc-body"):
#     print ('======[',count,']=========')
#     news_title = item.select(".esc-lead-article-title")[0].text
#     news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
#     print (news_title)
#     print (news_url)
#     count += 1

# url = "https://www.google.com/search?q=土石流+pdf"
# res = requests.get(url)
# soup = BeautifulSoup(res.content, "lxml")

# count = 1
# for item in soup.find_all("div",{"class":"g"}):
#     print ('======[',count,']=========')
#     print(item)
#     # news_title = item.select(".esc-lead-article-title")[0].text
#     # news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
#     # print (news_title)
#     # print (news_url)
#     count += 1

url = "http://csditn.tainan.gov.tw/web/wp-content/uploads/2016/05/Mudslide-Disaster-strain.pdf"
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")
print(soup)