#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if the platform is windows, type "chcp 65001" in the cmd line is nessasary
# for mac users, use the header "#!/usr/bin/env python3"




import pandas
import time
from appledaily import Appledaily


key_words=["水災","降雨","土石","水量","淹水","水"]

apple=Appledaily(key_words)

apple_list=apple.craw()
df=pandas.DataFrame(apple_list)
df.to_csv("output.csv")