#!/usr/bin/env python3
import jieba
import requests
import re
from bs4 import BeautifulSoup
from special_words import *
from operator import itemgetter

sec = Special_words().tw_sector()
city = Special_words().city_mark()
highway = Special_words().highway_mark()
landmark = Special_words().land_mark()
road = Special_words().road_mark()

name = highway["RoadName"]
h_name = []
for item in name:
    if item not in h_name:
        h_name.append(item)

name = landmark["Place_name"]
l_name = []
for item in name:
    # if item not in l_name:
    l_name.append(item)

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

    def article(self):
        r=requests.get(self.url)
        c=r.content
        soup=BeautifulSoup(c,"lxml")
        main_article=soup.find_all("div",{"class":"articulum trans"})
        text=main_article[0].text
        
        all_target = []

        find_highway = []
        for item in h_name:
            for m in re.finditer(item, text):
                all_target.append([item, m.start(), 3])
        

        find_city = []
        for item in city:
            for m in re.finditer(item, text):
                all_target.append([item, m.start(), 1])
        
        find_sec = []
        for item in sec:
            for m in re.finditer(item, text):
                cnt = 0
                for pair in find_sec:
                    if pair[1] == m.start():
                        cnt+=1
                if cnt < 1:       
                    all_target.append([item, m.start(), 2])
     
        
        


        # all_target=sorted(all_target,key=itemgetter(0));
        return all_target
        # return(text)
    

    def test(self):
        return l_name

# url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132663/【更新】暴雨影響%E3%80%807公路路段今下午仍封閉"
url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132679/雨勢大%E3%80%80南投、高雄部分地區列淹水一級警戒"
test = Apple_explicit(url)
# all = test.jie_do()
article = test.article()
y=sorted(article,key=itemgetter(1));
print(y)
# print(all)
# highway_name = test.test()
# print(highway_name)
# for m in re.finditer('台20線', article):
#     print('台20線', m.start())
# print(re.finditer('台20線', article))
# print(article.find("台20線"))
# print(article)