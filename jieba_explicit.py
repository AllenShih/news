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



r_name = []
for item in road:
    r_name.append(item[3])

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
        
        return(text)
    

    def find_key(self,article):
        all_target = []

        erase_words = ["太平洋","南部","北部","東部","西部","菜市場","中間","花園","上大","部地","西南","大坑"]
        for words in erase_words:
            article = article.replace(words, " "*len(words))

        text = article
        find_city_C = []
        for item in city:
            for m in re.finditer(item, text):
                find_city_C.append([item,m.start(),"C"])
                text = text.replace(item, " "*len(item))
        find_city_C=sorted(find_city_C,key=itemgetter(1))

        find_sec_C = []
        for item in sec:
            if len(item)>=3:
                search_word=[item,item[:-1]]
                for word in search_word:
                    for m in re.finditer(word, text):
                        find_sec_C.append([item,m.start(),"S"])
                        text = text.replace(word, " "*len(item))
            else:
                for m in re.finditer(item, text):   
                    find_sec_C.append([item,m.start(),"S"])
                    text = text.replace(item, " "*len(item))
        find_sec_C=sorted(find_sec_C,key=itemgetter(1))

        
        find_highway_C = []
        for item in h_name:
            for m in re.finditer(item, text):
                left_bracket = text.find("(",m.start())
                right_bracket = text.find(")",m.start())
                numbers = text[left_bracket:right_bracket+1]
                find_highway_C.append([item,m.start(),"H",numbers])
                text = text.replace(item, " "*len(item))
               
        # if len(find_highway_C) != 0:

        find_highway_C=sorted(find_highway_C,key=itemgetter(1))


        # find_landmark = []
        # for item in l_name:
        #     for m in re.finditer(item, text):
        #         find_landmark.append(item+"-"+str(m.start()))
        #         text = text.replace(item, " "*len(item))
        
        find_road_C = []
        for item in r_name:
            for m in re.finditer(item, text):
                find_road_C.append([item,m.start(),"R"])
                text = text.replace(item, " "*len(item))
        find_road_C=sorted(find_road_C,key=itemgetter(1))

        all_target.append(find_city_C)
        all_target.append(find_sec_C)
        all_target.append(find_highway_C)
        # all_target.append(find_landmark)
        all_target.append([ ])
        all_target.append(find_road_C)
        # all_target = sorted(all_target, key=itemgetter(1))
        return all_target

#-------------------------------------------------------------------------------------------------------------------------------
url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132663/【更新】暴雨影響%E3%80%807公路路段今下午仍封閉"
# url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132679/雨勢大%E3%80%80南投、高雄部分地區列淹水一級警戒"
test = Apple_explicit(url)
article = test.article()
target = test.find_key(article)
if len(target[2]) != 0:
    for item in target[2]:
        # print(item[1])
        # left = article.find("(",item[1])
        # right = article.find(")",item[1])
        # print("-----------------")
        # print(article[left:right+1])
        
        # print(item[1])
        print(item)

# print(len(target[2]))

#-------------------------------------------------------------------------------------------------------------------------------

# text = "這台9線波梅雨造成台灣各地雨勢不斷台8線,"
# find_highway = []
# for item in h_name:
#     for m in re.finditer(item, text):
#         find_highway.append([item, m.start()])
#         # find_highway.append(item+"-"+str(m.start()))
#         text = text.replace(item, " "*len(item))
# y=sorted(find_highway,key=itemgetter(1));
# print(y)
# for i in range(len(l_name)):
#     print(len(l_name))
#     # print(re.finditer(l_name[i], text))
    # for m in re.finditer(l_name[i], text):
    #     print(m)
        # find_landmark.append(l_name[i]+"-"+str(m.start()))
        # text = text.replace(l_name[i], " "*len(l_name[i]))


        

# highway_name = test.test()
# print(highway_name)
# for m in re.finditer('台20線', article):
#     print('台20線', m.start())
# print(re.finditer('台20線', article))
# print(article.find("台20線"))
# print(article)