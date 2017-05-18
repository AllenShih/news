#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"




import pandas
import time
from newspaper import *
from database import Database

key_words=["水災","降雨","土石","水量","淹水","水","雨","坍方"]

dbname = " dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432' "

database = Database(dbname)


Apple=Appledaily(key_words,database).craw()

Liberty = LibertyTimes(key_words,database).craw()

Udn = Udn(key_words,database).craw()


