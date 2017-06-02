#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from database import Database

from datetime import date

# dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

# database = Database(dbname)

# # database.insert("蘋果日報","title","date+" "+time","category","url")

# l=database.search(title="(151551))")
# print(l)

dat= "2017 / 06 / 02 12:21"
print(dat.replace(" / ","-"))