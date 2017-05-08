# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Appledaily:
    def __init__(self,key_words):
        self.key_words=key_words
        

    def craw(self):
        cnt=0
        l=[]
        url="http://www.appledaily.com.tw/realtimenews/section/new/"
        while cnt<15:
            cnt+=1
            print(cnt)
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
                    life_news=news_all[i].find_all("li",{"class":"rtddt life"})+ \
                    news_all[i].find_all("li",{"class":"rtddt life even"})+news_all[i].find_all("li",{"class":"rtddt life even hsv"})
                    for lines in life_news:
                        d={}
                        href_back=lines.find('a').get('href')
                        href=hr+href_back
                        time=lines.find_next('time').text
                        category=lines.find_next('h2').text
                        title=lines.find_next('h1').text

                        word_cnt=0
                        for words in self.key_words:
                            if words in title:
                                word_cnt+=1
                        if word_cnt>0:
                            d["新聞來源"]="蘋果日報"
                            d["Time"]=date+" "+time
                            d["Category"]=category
                            d["Title"]=title
                            d["URL"]=href
                            l.append(d)
        return l
