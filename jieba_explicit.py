#!/usr/bin/env python3
import jieba
import requests
from bs4 import BeautifulSoup

class Apple_explicit:

    def __init__(self,url):
        self.url = url
    
    def jie_do(self):
        r=requests.get(self.url)
        c=r.content
        soup=BeautifulSoup(c,"lxml")
        main_article=soup.find_all("div",{"class":"articulum trans"})
        jieba.set_dictionary('dict.txt.big')
        text=main_article[0].text

        jieba.suggest_freq("土石流", True)
        jieba.suggest_freq("中颱", True)
        jieba.suggest_freq("強颱", True)
        jieba.suggest_freq("全台", True)
        newlist=[]
        seglist = jieba.cut(text, cut_all = False)
        for item in seglist:
            if item=="googletag":
                break
            else:
                newlist.append(item)
        return (newlist)
        # print (newlist)
            # print(item)

# url = "http://www.appledaily.com.tw/realtimenews/article/life/20170603/1132476/北市又現強降雨　災情數達600件"
# test = Apple_explicit(url)
# test.jie_do()