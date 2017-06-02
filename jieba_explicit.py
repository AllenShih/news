#!/usr/bin/env python3
import jieba
import requests
from bs4 import BeautifulSoup

class Jieba_explicit:

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

        seglist = jieba.cut(text, cut_all=False)
        for item in seglist:
            if item=="googletag":
                break
            print(item)

url = "http://www.appledaily.com.tw/realtimenews/article/life/20170602/1131510/阿里山公路零星落石%E3%80%80晚上8時起預警性封閉"
test = Jieba_explicit(url)
test.jie_do()