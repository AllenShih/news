#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database
import pandas as pd
from special_words import *
import jieba
import requests
import re
from bs4 import BeautifulSoup
from special_words import *
from operator import itemgetter
from jieba_explicit import *


dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

database = Database(dbname)

data = pd.read_csv("apple20170605.csv")
new_data = []
with open("apple20170605.csv", encoding='utf8') as w:
    content = w.readlines()
    for lines in content:

        split_line = lines.split(";")
        new_data.append(split_line[:5])

# print(new_data[0][4])

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
    combine = ""
    combine_hw = ""
    for word in all_key[0]:
        city = city + word[0] + " "
        comb_add.append(word)
    for word in all_key[1]:
        sec = sec + word[0] + " "
        comb_add.append(word)
    for word in all_key[2]:
        highway = highway + word[0] + word[3] + " " 
        comb_hw.append(word)
    # for item in all_key[3]:
    #     landmark = landmark+item[0]+" "
    for word in all_key[4]:
        road = road + word[0] + " "
        comb_add.append(word)

    comb_add = sorted(comb_add, key=itemgetter(1))
    for word in comb_add:
        if word[2] == "C" and len(combine) != 0:
            combine = combine + "," + word[0]
        elif word[2] == "S":
            if len(combine) == 0:
                combine = combine + word[0]
            elif combine[-1] == ",":
                combine = combine + word[0]
            else:
                combine = combine + "-" + word[0]
        elif word[2] == "R":
            if len(combine) == 0:
                combine = combine + word[0]
            elif combine[-1] == ",":
                combine = combine + word[0]
            else:
                combine = combine + "-" + word[0]
        elif word[2] == "C":
            combine = combine + word[0]
    

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
            if len(k_part_num)==1:
                k_part_num = "0"+k_part_num
            k_part = k_part_num +"K"+"+000"
            combine_hw = combine_hw + " " + k_part
            # print(combine_hw)
        else:
            if plus in item_1[3]:
                sp_2 = item_1[3].split(plus)
                p_part = sp_2[1]
                if int(p_part)>250:
                    p_part = "500"
                else:
                    p_part = "000"
                    
                k_part = sp_2[0]
                if k_part[0] == "0" and len(k_part) > 3:
                    k_part = k_part[1:]
                elif k_part[0] != "0" and len(k_part) == 2:
                    k_part = "0" + k_part

                k_part = k_part[:-1] +"K+"+ p_part
                combine_hw = combine_hw + " " + k_part
                # print(combine_hw)
            else:
                k_part = item_1[3]
                if k_part[0] == "0" and len(k_part) > 3:
                    k_part = k_part[1:] + "+000"
                elif k_part[0] != "0" and len(k_part) == 2:
                    k_part = "0" + k_part + "+000"
                else:
                    k_part = k_part + "+000"
                combine_hw = combine_hw + " " + k_part
                # print(combine_hw)
    database.insert(item[0],item[1],item[2],item[3],item[4], city, sec, highway, combine_hw, road, combine)
