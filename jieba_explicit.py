#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup
from special_words import *
from operator import itemgetter
from database import *
from geocodeQuery import GeocodeQuery

sec = Special_words().tw_sector()
city = Special_words().city_mark()
highway = Special_words().highway_mark()
landmark = Special_words().land_mark()
road = Special_words().road_mark()
highway_pd = highway

name = highway["RoadName"]
h_name = []
for item in name:
    if item not in h_name:
        h_name.append(item)

# name = landmark["Place_name"]
# l_name = []
# for item in name:
#     # if item not in l_name:
#     l_name.append(item)
# print(landmark)
# # r_name = []
# # for item in road:
# #     r_name.append(item[:-1])

# print(road)

class article_grab:

    def __init__(self,url):
        self.url = url

    def apple_article(self):
        r=requests.get(self.url)
        c=r.content
        soup=BeautifulSoup(c,"lxml")
        main_article=soup.find("div",{"class":"ndArticle_margin"})
        text = main_article.find("p").text        
        return(text)

    def liberty_article(self):
        r=requests.get(self.url)
        c=r.content
        soup=BeautifulSoup(c,"lxml")
        main_article=soup.find("div",{"class":"text"})
        text_all = main_article.find_all("p")
        text = ""
        for item in text_all:
            text = text + item.text       
        return(text)
    
    def chinatimes_article(self):
        r=requests.get(self.url)
        c=r.content
        soup=BeautifulSoup(c,"lxml")
        main_article=soup.find("div",{"class":"clummbox clear-fix"})
        text_all = main_article.find_all("p")
        text = ""
        for item in text_all:
            text = text + item.text       
        return(text)

    def find_key(self,article):
        all_target = []
        find_city_C = []
        find_sec_C = []
        find_highway_C = []
        find_landmark_C = []
        find_road_C = []

        text = article
        
        # words of road that needs to be search first 
        road_first = ["大湖山莊街"]
        for item in road_first:
            for m in re.finditer(item, text):
                find_road_C.append([item,m.start(),"R"])
                text = text.replace(item, " "*len(item))
        find_road_C=sorted(find_road_C,key=itemgetter(1))

        # words that needs to be erase first
        erase_words = ["太平洋","南部","北部","東部","西部","菜市場","中間","花園","上大","部地","西南","大坑","市場","新路","河川"]
        for words in erase_words:
            text = text.replace(words, " "*len(words))

        for item in city:
            for m in re.finditer(item, text):
                find_city_C.append([item,m.start(),"C"])
                text = text.replace(item, " "*len(item))
        find_city_C=sorted(find_city_C,key=itemgetter(1))

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

        word_find = re.compile("[1234567890kK~+]")
        for item in h_name:
            for m in re.finditer(item, text):
                match = word_find.finditer(text,m.end())
                cnt = 0
                for w in match:
                    if cnt==0:
                        ini = w.start()
                        last_id = w.start()
                    cnt+=1    
                    # print(cnt)
                    if (w.start()-last_id)<=1:
                        end = w.end()
                        last_id = w.start()
                numbers = text[ini:end]
                find_highway_C.append([item,m.start(),"H",numbers])
                text = text.replace(item, " "*len(item))
        find_highway_C=sorted(find_highway_C,key=itemgetter(1))

        # for item in landmark:
        #     if item in text:
        #         for m in re.finditer(item, text):
        #             find_landmark_C.append([item,m.start(),"L"])
        #             text = text.replace(item, " "*len(item))
        # find_landmark_C=sorted(find_landmark_C,key=itemgetter(1))

        for item in road:
            if item in text:
                for m in re.finditer(item, text):
                    find_road_C.append([item,m.start(),"R"])
                    text = text.replace(item, " "*len(item))
        find_road_C=sorted(find_road_C,key=itemgetter(1))

        all_target.append(find_city_C)
        all_target.append(find_sec_C)
        all_target.append(find_highway_C)
        all_target.append(find_landmark_C)
        # all_target.append([ ])
        all_target.append(find_road_C)
        # all_target = sorted(all_target, key=itemgetter(1))
        return all_target

class data_check:
    def __init__(self,Database,article,newspaper,title,dtime,category,href):
        self.article = article
        self.newspaper = newspaper
        self.title = title
        self.dtime = dtime
        self.category = category
        self.href = href
        self.database = Database
        # self.database.insert_location(self.newspaper,self.title,self.dtime,"addre","inp")

    def check(self,all_target):
        all_key = all_target
        word_cnt = 0 #check if this paragraph is addnig anything
        highway_coor_lon = []
        highway_coor_lat = []
        add_coor_lon = []
        add_coor_lat = []
        city = ""
        sec = ""
        highway = ""
        landmark = ""
        road = ""
        comb_add = []
        comb_hw = []
        hw_name = []
        hw_num = []
        combine = ""
        combine_ls = []
        combine_hw = ""
        comb_hw_ls= []
        coor_all = ""
        for word in all_key[0]:
            city = city + word[0] + " "
            comb_add.append(word)
        for word in all_key[1]:
            sec = sec + word[0] + " "
            comb_add.append(word)
        for word in all_key[2]:
            highway = highway + word[0] + word[3] + " " 
            comb_hw.append(word)
            hw_name.append(word[0])
        for word in all_key[3]:
            landmark = landmark+word[0]+" "
        for word in all_key[4]:
            road = road + word[0] + " "
            comb_add.append(word)

    # combining all the address
        comb_add = sorted(comb_add, key=itemgetter(1))
        last_sign = "None"
        last_city = "None"
        last_sec = "None"
        for word in comb_add:
            if word[2] == "C" and len(combine) != 0:
                combine = combine + "," + word[0]
                last_city = word[0]
            elif word[2] == "S":
                last_sec = word[0]
                if len(combine) == 0:
                    combine = combine + word[0]
                elif last_sign == "C":
                    combine = combine + word[0]
                elif last_sign == "S" and last_city != "None":
                    combine = combine + "," + last_city + word[0]
                elif last_sign == "S" and last_city == "None":
                    combine = combine + "," + word[0]
                elif last_sign == "R" and last_city != "None":
                    combine = combine + "," + last_city + word[0]
                elif last_sign == "R" and last_city == "None":
                    combine = combine + "," + word[0]
                else:
                    combine = combine + "," + word[0]
            elif word[2] == "R":
                if len(combine) == 0:
                    combine = combine + word[0]
                elif last_sign == "C" and last_sec != "None":
                    combine = combine + last_sec + word[0]
                elif last_sign == "C" and last_sec == "None":
                    combine = combine + word[0]
                elif last_sign == "S" :
                    combine = combine + word[0]
                elif last_sign == "R" and last_sec != "None":
                    combine = combine + "," + last_sec + word[0]
                elif last_sign == "R" and last_sec == "None":
                    combine = combine + "," + word[0]
                else:
                    combine = combine + "," + word[0]
            elif word[2] == "C":
                combine = combine + word[0]
                last_city = word[0]
            last_sign = word[2]
    
        combine_ls = combine.split(",")
        # print(combine_ls)
        new_coor = []
        repeat_check = []
        for addre in combine_ls:
            if len(addre)>1 and addre not in repeat_check:
                repeat_check.append(addre)
                gq = GeocodeQuery("zh-tw", "tw")
                gq.get_geocode(addre)
                temp_lat = gq.get_lat()
                temp_lon = gq.get_lng()
                inp = "["+ str(temp_lat) +","+ str(temp_lon) +"]"

                add_coor_lat.append(temp_lat)
                add_coor_lon.append(temp_lon)
                
                new_coor.append(inp)
                self.database.insert_location(self.newspaper,self.title,self.dtime,addre,inp)
                word_cnt += 1
            all_new_coor = " ".join(new_coor)
            # print(all_new_coor)

        for item_1 in comb_hw:
            wave = "~"
            plus = "+"
            if wave in item_1[3]:
                sp_1 = item_1[3].split(wave)
                num = 0
                for part in sp_1:
                    if plus in part:
                        sp_2 = part.split(plus)
                        k_part = sp_2[0]
                        p_part = sp_2[1]
                        num = num + int(k_part[:-1])
                    else:
                        num = num + int(part[:-1])
                k_part_num = str(int(num/2))
                k_part = k_part_num +"K"+"+000"
                
                combine_hw = combine_hw + " " + k_part
                hw_num.append(k_part)
                # print(comb_hw_ls)
            else:
                if plus in item_1[3]:
                    sp_2 = item_1[3].split(plus)
                    p_part = sp_2[1]
                    if int(p_part)>250:
                        p_part = "500"
                    else:
                        p_part = "000"
                        
                    k_part = sp_2[0][:-1]
                    k_part = str(int(k_part))

                    k_part =  k_part + "K+" + p_part
                    
                    combine_hw = combine_hw + " " + k_part
                    hw_num.append(k_part)
                    # print(comb_hw_ls)
                else:
                    k_part = item_1[3][:-1]
                    k_part = str(int(k_part))
                    k_part = k_part + "K+000"
                    
                    combine_hw = combine_hw + " " + k_part
                    hw_num.append(k_part)
        for i in range(len(hw_name)):
            lat = highway_pd.loc[highway_pd['Stake'] == hw_num[i]].loc[highway_pd['RoadName'] == hw_name[i], "latitude"].values[0]
            lon = highway_pd.loc[highway_pd['Stake'] == hw_num[i]].loc[highway_pd['RoadName'] == hw_name[i], "longitude"].values[0]
            coor = [lat,lon]
            coor_exp = "["+ str(lat) +","+str(lon)+"]"
            coor_all = coor_all+" "+coor_exp
            highway_coor_lat.append(lat)
            highway_coor_lon.append(lon)
            full_highway = hw_name[i]+" "+hw_num[i]
            self.database.insert_location(self.newspaper,self.title,self.dtime,full_highway,coor_exp)
            word_cnt += 1
        if word_cnt == 0 :
            self.database.insert_location(self.newspaper,self.title,self.dtime,"Empty","Empty")

#-------------------------------------------------------------------------------------------------------------------------------
# # url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132663/【更新】暴雨影響%E3%80%807公路路段今下午仍封閉"
# # url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132679/雨勢大%E3%80%80南投、高雄部分地區列淹水一級警戒"
# # url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132918/暴雨襲台道路坍方　目前仍有7處未搶通"
# url = "http://www.appledaily.com.tw/realtimenews/article/life/20170604/1132779/梅雨鋒面漸北移　北市府災變中心改三級開設"
# url = "https://tw.news.appledaily.com/life/realtime/20180517/1355415/"
# test = Apple_explicit(url)
# article = test.article()
# target = test.find_key(article)
# # print(article)
# print(target)
# if len(target[1]) != 0:
#     for item in target[4]:
#         # print(item[1])
#         # left = article.find("(",item[1])
#         # right = article.find(")",item[1])
#         # print("-----------------")
#         # print(article[left:right+1])
        
#         # print(item[1])
#         print(item)

# print(road)
# # print(len(target[2]))

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