# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from database import Database

class Appledaily:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database
        

    def craw(self):
        print("蘋果日報")
        cnt=0
        l=[]
        url="http://www.appledaily.com.tw/realtimenews/section/new/"
        while cnt<50:
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
                            self.database.insert("蘋果日報",title,date+" "+time,category,url)


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
                url=all_a[1].get('href')
                
                word_cnt=0
                for words in self.key_words:
                    if words in title:
                        word_cnt+=1
                if word_cnt>0:
                    self.database.insert("自由時報",title,time,category,url)

class udn:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database

    def craw(self):
        print("聯合報")
        cnt=0
        l=[]
        udn_url="https://udn.com/news/breaknews/1/0/"

        base_url="https://udn.com"
        while cnt<30:    
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
                    self.database.insert("聯合報",title,time,category,url)