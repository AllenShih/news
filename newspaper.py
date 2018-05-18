# -*- coding: utf-8 -*-
import requests
from jieba_explicit import *
from special_words import *
from bs4 import BeautifulSoup
# from database import *
from database_ms import Database_ms
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
        url="https://tw.appledaily.com/new/realtime/"
        while cnt<5:
            cnt+=1
            print(cnt)
            r=requests.get(url+str(cnt))
            c=r.content
            soup=BeautifulSoup(c,"lxml")

            all_content=soup.find_all("div",{"class":"abdominis rlby clearmen"})

            # hr="http://www.appledaily.com.tw"

            for article in all_content:
                date_all=article.find_all("h1",{"class":"dddd"})
                news_all=article.find_all("ul",{"class":"rtddd slvl"})
                for i in range(len(news_all)):
                    date=date_all[i].text.replace(" / ","-")
                    life_news=news_all[i].find_all("li",{"class":"rtddt life"})+ \
                    news_all[i].find_all("li",{"class":"rtddt life even"})+news_all[i].find_all("li",{"class":"rtddt life even hsv"})
                    for lines in life_news:
                        d={}
                        href=lines.find('a').get('href')
                        # href=hr+href_back
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
                                para = article_grab(href).apple_article()
                                all_target = article_grab(href).find_key(para)
                                data_check(self.database,para,"蘋果日報",title,date+" "+time,category,href).check(all_target)
                                self.database.insert_just_news("蘋果日報",title,date+" "+time,category,href)
                           


class LibertyTimes:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database

    def craw(self):
        print("自由時報")
        cnt=0
        l=[]
        url="http://news.ltn.com.tw/list/breakingnews/all/"
        while cnt<5:
            
            cnt+=1
            print(cnt)
            r=requests.get(url+str(cnt))
            c=r.content
            soup=BeautifulSoup(c,"lxml")

            all_content=soup.find("ul",{"class":"list imm"})
            all_article = all_content.find_all("li")
            for article in all_article:
                d={}
                time=article.find("span").text
                all_a=article.find_all('a', href=True)
                category=article.find("div",{"class":"tagarea"}).text
                title=all_a[1].text
                href=all_a[1].get('href')
                if len(time)<6:
                    date_time = str(date.today())+" "+time
                # print(title)
                word_cnt=0
                for words in self.key_words:
                    if words in title:
                        # print(title)
                        word_cnt+=1
                if word_cnt>0:
                    if(self.database.search(title=title) == []):
                        para = article_grab(href).liberty_article()
                        all_target = article_grab(href).find_key(para)
                        data_check(self.database,para,"自由時報",title[6:],date_time,category,href).check(all_target)
                        self.database.insert_just_news("自由時報",title[6:],date_time,category,href)


class Chinatimes:
    def __init__(self,key_words,Database):
        self.key_words=key_words
        self.database=Database
    def craw(self):
        print("中國時報")
        cnt=0
        l=[]
        url="http://www.chinatimes.com/realtimenews?page="
        base_url = "http://www.chinatimes.com"
        while cnt<5:
            
            cnt+=1
            print(cnt)
            r=requests.get(url+str(cnt))
            c=r.content
            soup=BeautifulSoup(c,"lxml")
            all_content = soup.find("div",{"class":"listRight"})
            all_article = all_content.find_all("li",{"class":"clear-fix"})
            for article in all_article:
                d={}
                title = article.find("h2").find("a", href = True).text
                href = article.find("h2").find("a", href = True).get("href")
                time = article.find("time").text
                category = article.find("div",{"class" : "kindOf"}).text
                just_time = time[0:5]
                just_date = time[6:].replace("/","-")
                final_datetime = just_date+" "+just_time
                word_cnt=0
                for words in self.key_words:
                    if words in title:
                        # print(title)
                        word_cnt+=1
                if word_cnt>0:
                    if(self.database.search(title=title) == []):
                        para = article_grab(base_url+href).chinatimes_article()
                        all_target = article_grab(href).find_key(para)
                        data_check(self.database,para,"中國時報",title,final_datetime,category,base_url+href).check(all_target)
                        self.database.insert_just_news("中國時報",title,final_datetime,category,base_url+href)