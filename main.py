# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary

import appledaily
import requests
from bs4 import BeautifulSoup
import csv

key_words=["水災","降雨"]

K = open("新聞資料.csv","w",newline='')
w = csv.writer(K)
top_row=['Title', 'Time', 'category', 'URL']
w.writerow(top_row)

url="http://www.appledaily.com.tw/realtimenews/section/new/"
cnt=0
while True:
    cnt+=1
    r=requests.get(url+str(cnt))
    c=r.content
    soup=BeautifulSoup(c,"lxml")

    all=soup.find_all("div",{"class":"abdominis rlby clearmen"})

    hr="http://www.appledaily.com.tw/"
    for article in all:
        news=article.find_all("li",{"class":"rtddt life"}) +article.find_all("li",{"class":"rtddt life even"}) +article.find_all("li",{"class":"rtddt life even hsv"} )
        for lines in news:
            # print(lines.text)
            href_back=lines.find('a').get('href')
            href=hr+href_back
            time=lines.find_next('time').text
            category=lines.find_next('h2').text
            title=lines.find_next('h1').text
            row=[title,time,category,href]
            w.writerow(row)
            print(href)
            print(time)
            print(category)
            print(title)
            # links=lines.find_all("a")
            # for href in links:
            #     href=href.get('href')
            #     Entire_link=hr+href
            #     print(Entire_link)
