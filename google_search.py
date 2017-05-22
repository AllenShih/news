#!/usr/bin/env python3
# -*- coding: utf8 -*-


import requests
from bs4 import BeautifulSoup

key_words="土石流+pdf"
url = "https://www.google.com/search?q="+key_words
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")

count = 1
for item in soup.find_all("div",{"class":"g"}):
    print ('======[',count,']=========')
    print(item)
    # news_title = item.select(".esc-lead-article-title")[0].text
    # news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
    # print (news_title)
    # print (news_url)
    count += 1