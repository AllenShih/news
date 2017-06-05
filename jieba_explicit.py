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

url = "http://www.appledaily.com.tw/realtimenews/article/life/20170603/1132351/%E3%80%90%E6%B7%B9%E6%B0%B4%E7%89%87%E3%80%91%E9%8B%92%E9%9D%A2%E5%8C%97%E7%A7%BB%20%E6%B7%A1%E6%B0%B4%E4%B8%AD%E6%AD%A3%E6%9D%B1%E8%B7%AF%E5%8F%88%E6%B7%B9%E4%BA%86"
test = Apple_explicit(url)
all = test.jie_do()
print(all)