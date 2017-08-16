#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import *
import pandas as pd
from special_words import *
import jieba
import requests
import re
from bs4 import BeautifulSoup
from special_words import *
from operator import itemgetter
from jieba_explicit import *
from geocodeQuery import GeocodeQuery


dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

database = Database(dbname)
database_2 = Database2(dbname)


data = pd.read_csv("apple20170605.csv")
new_data = []
with open("apple20170605.csv", encoding='utf8') as w:
    content = w.readlines()
    for lines in content:

        split_line = lines.split(";")
        new_data.append(split_line[:5])

# print(new_data[0][4])

highway_pd = Special_words().highway_mark()

for item in new_data:
    # item[4] is url
    para = Apple_explicit(item[4])
    article = para.article()
    all_key = para.find_key(article)
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
    for addre in combine_ls:
        if len(addre)>1:
            gq = GeocodeQuery("zh-tw", "tw")
            gq.get_geocode(addre)
            inp = "["+ str(gq.get_lat()) +","+str(gq.get_lng())+"]"
            new_coor.append(inp)
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
                # print(comb_hw_ls)
    # print(hw_num)
    # print(hw_name)
    database.insert(item[0],item[1],item[2],item[3],item[4], city, sec, highway, landmark , road, combine, combine_hw, coor_all,all_new_coor)
    database_2.insert(item[1], highway, combine, combine_hw, coor_all, all_new_coor)
# print(highway_pd)

