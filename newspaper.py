# -*- coding: utf-8 -*-
import requests
from jieba_explicit import *
from special_words import *
from bs4 import BeautifulSoup
from database import *
from datetime import date

class Appledaily:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database
        

    def craw(self):
        # tw_sec = Special_words().tw_sector()
        # sp_loc = Special_words().special_location() 
        # addr = Special_words().address()
        print("蘋果日報")
        cnt=0
        l=[]
        url="http://www.appledaily.com.tw/realtimenews/section/new/"
        while cnt<60:
            cnt+=1
            print(cnt)
            r=requests.get(url+str(cnt))
            c=r.content
            soup=BeautifulSoup(c,"lxml")

            all=soup.find_all("div",{"class":"abdominis rlby clearmen"})

            hr="http://www.appledaily.com.tw"

            for article in all:
                date_all=article.find_all("h1",{"class":"dddd"})
                news_all=article.find_all("ul",{"class":"rtddd slvl"})
                for i in range(len(news_all)):
                    date=date_all[i].text.replace(" / ","-")
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
                        sec = []
                        location = []
                        for words in self.key_words:
                            if words in title:
                                # print(title)
                                word_cnt+=1
                        if word_cnt>0:
                             if(self.database.search(title=title) == []):
                                # para = Apple_explicit(href)
                                # article = para.article()
                                
                                # all_key = para.find_key(article)
                                # city = " ".join(all_key[0])
                                # sec = " ".join(all_key[1])
                                # highway = " ".join(all_key[2])
                                # landmark = " ".join(all_key[3])
                                # road = " ".join(all_key[4])
                                self.database.insert("蘋果日報",title,date+" "+time,category,href)
                           


class LibertyTimes:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database

    def craw(self):
        print("自由時報")
        cnt=0
        l=[]
        url="http://news.ltn.com.tw/list/BreakingNews?page="
        while cnt<50:
            
            cnt+=1
            print(cnt)
            r=requests.get(url+str(cnt))
            c=r.content
            soup=BeautifulSoup(c,"lxml")

            all=soup.find_all("li",{"class":"lipic"})
            
            for detail in all:
                d={}
                time=detail.find("span").text
                all_a=detail.find_all('a', href=True)
                category=all_a[0].get('href')
                title=all_a[1].text
                href=all_a[1].get('href')
                
                word_cnt=0
                for words in self.key_words:
                    if words in title and category=="/list/life":
                        # print(title)
                        word_cnt+=1
                if word_cnt>0:
                    if(self.database.search(title=title) == []):
                        self.database.insert("自由時報",title,time,category,href)

class Udn:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database

    def craw(self):
        print("聯合報")
        cnt=0
        l=[]
        udn_url="https://udn.com/news/breaknews/1/0/"

        base_url="https://udn.com"
        while cnt<100:    
            cnt+=1
            print(cnt)
            r=requests.get(udn_url+str(cnt)+"#breaknews")
            c=r.content
            soup=BeautifulSoup(c,"lxml")

            all=soup.find("div",{"id":"breaknews_body"})
            all_article=all.find_all("dt")

            for detail in all_article:
                d={}
                category = detail.find("a",{"class":"cate"}).text
                h2 = detail.find("h2")
                title = h2.text
                url = base_url+h2.find_next("a").get("href")
                time = detail.find("div",{"class":"dt"}).text
                # print(title)
                word_cnt=0
                for words in self.key_words:
                    if words in title:
                        word_cnt+=1
                if word_cnt>0:
                    if(self.database.search(title=title) == []):
                        self.database.insert("聯合報",title,str(date.today().year)+"-"+time,category,url)

class Ettoday:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database
    def craw(self):
        print("東森新聞網")
        cnt=0
        l=[]
        udn_url="https://udn.com/news/breaknews/1/0/"

        base_url="https://udn.com"
        while cnt<50:    
            cnt+=1
            print(cnt)
            r=requests.get(udn_url+str(cnt)+"#breaknews")
            c=r.content
            soup=BeautifulSoup(c,"lxml")