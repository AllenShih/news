#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from database import Database

# from datetime import date

# dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

# database = Database(dbname)

# # database.insert("蘋果日報","title","date+" "+time","category","url")

# l=database.search(title="(151551))")
# print(l)

# dat= "2017 / 06 / 02 12:21"
# print(dat.replace(" / ","-"))

import pandas as pd

# df = pd.read_csv("臺灣省道編號座標.csv")

# print(df['Stake'])

# df2 = pd.read_csv("臺灣地區地名資料_具有地標意義公共設施類20161130.csv")

# print(df2['X'])

with open("dict.txt.big") as f:
    content = f.readlines()
    for item in content:
        print(item.split(" "))