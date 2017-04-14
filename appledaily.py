# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.appledaily.com.tw/realtimenews/section/new/")
c=r.content
soup=BeautifulSoup(c,"lxml")

all=soup.find_all("div",{"class":"abdominis rlby clearmen"})

hr="http://www.appledaily.com.tw/"
for article in all:
    news=article.find_all("li",{"class":"rtddt life"} )+article.find_all("li",{"class":"rtddt life even"} )+article.find_all("li",{"class":"rtddt life enen hsv"} )
    for lines in news:
        print(lines.text)
        links=lines.find_all("a")
        # for href in links:
        #     href=href.get('href')
        #     Entire_link=hr+href
        #     print(Entire_link)
