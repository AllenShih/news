# -*- coding: utf-8 -*-
# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"

import appledaily
import requests
from bs4 import BeautifulSoup
import csv
import pandas

key_words=["水災","降雨"]

url="http://www.appledaily.com.tw/realtimenews/section/new/"
cnt=0

l=[]
while cnt<13:
    cnt+=1
    r=requests.get(url+str(cnt))
    c=r.content
    soup=BeautifulSoup(c,"lxml")

    all=soup.find_all("div",{"class":"abdominis rlby clearmen"})

    hr="http://www.appledaily.com.tw/"

    for article in all:
        date_all=article.find_all("h1",{"class":"dddd"})
        news_all=article.find_all("ul",{"class":"rtddd slvl"})
        for i in range(len(news_all)):
            date=date_all[i].text
            life_news=news_all[i].find_all("li",{"class":"rtddt life"})+news_all[i].find_all("li",{"class":"rtddt life even"})+news_all[i].find_all("li",{"class":"rtddt life even hsv"})
            for lines in life_news:
                d={}
                href_back=lines.find('a').get('href')
                href=hr+href_back
                time=lines.find_next('time').text
                category=lines.find_next('h2').text
                title=lines.find_next('h1').text
                d["Time"]=date+" "+time
                d["Category"]=category
                d["Title"]=title
                d["URL"]=href
                l.append(d)

df=pandas.DataFrame(l)
df.to_csv("output.csv")
