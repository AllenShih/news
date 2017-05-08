# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class LibertyTimes:
    def __init__(self,key_words):
        self.key_words=key_words


    def craw(self):
            cnt=0
            l=[]
            url="http://news.ltn.com.tw/list/BreakingNews?page="
            while cnt<10:
                
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
                        d["新聞來源"]="自由時報"
                        d["Title"]=title
                        d["Time"]=time
                        d["Category"]=category
                        d["URL"]=url
                        l.append(d)
            return l
                