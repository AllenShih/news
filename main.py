#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"




import pandas
import time
from newspaper import *
from database import Database
from special_words import Special_words

key_words=["水災","降雨","土石","降雨量","淹水","坍方","鋒面","暴雨"]

# S_words=Special_words()

# all_words = Special_words().tw_sector()
# all_words = all_words+ Special_words().special_location()
# for item in all_words:
#     print(item)

dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

database = Database(dbname)


Apple=Appledaily(key_words,database).craw()

# Liberty = LibertyTimes(key_words,database).craw()

# Udn = Udn(key_words,database).craw()

