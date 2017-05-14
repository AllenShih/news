#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"




import pandas
import time
from newspaper import *
from database import Database

key_words=["水災","降雨","土石","水量","淹水","水","雨"]

dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

database = Database(dbname)


apple=Appledaily(key_words,database).craw()
# apple_list=apple.craw()
# df1=pandas.DataFrame(apple_list)
# df1.to_csv("output1.csv")

Liberty = LibertyTimes(key_words,database).craw()
# liberty_list = Liberty.craw()
# df2=pandas.DataFrame(liberty_list)
# df2.to_csv("output2.csv")


udn = udn(key_words,database).craw()
# udn_list = udn.craw()
# df3=pandas.DataFrame(udn_list)
# df3.to_csv("output3.csv")