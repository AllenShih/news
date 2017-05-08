#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"




import pandas
import time
from appledaily import Appledaily
from libertytimes import LibertyTimes


key_words=["水災","降雨","土石","水量","淹水","水","教堂"]

apple=Appledaily(key_words)
apple_list=apple.craw()
df1=pandas.DataFrame(apple_list)
df1.to_csv("output1.csv")

Liberty = LibertyTimes(key_words)
liberty_list = Liberty.craw()
df2=pandas.DataFrame(liberty_list)
df2.to_csv("output2.csv")
