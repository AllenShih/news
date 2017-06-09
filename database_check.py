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

df = pd.read_csv("/Users/AllenShih/Desktop/news/%E7%9C%81%E9%81%93%E5%BA%A7%E6%A8%99.csv")

print(df)

