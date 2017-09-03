#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
# from special_words import *
# import pandas
# import csv
# with open("landmark_all.csv", encoding = "utf8") as w:
#     with open("landmark_new_.csv", "w", encoding="utf8") as f:
#         content = w.readlines()
#         for lines in content:
#             words = lines.split(",")
#             # print(words)
#             f.writelines(words[0]+"\n")
#             # print(words[0])
#             # print(lines)



delete_lines = ["山區" ,"中央氣象局","日月潭","公路總局","消防局","省道","活動中心","農委會","停車場","水閘","水利","冷泉","教育部","球場","公園","籃球場" ,"水利署","水系","營建署","經濟部","農糧署","交通部","國道","地下停車場","\""]
print(delete_lines)
with open("landmark_new_.csv", encoding = 'utf8') as w:
    with open("landmark_new_2.csv", "w", encoding="utf8") as f:
        content = w.readlines()
        for lines in content:
            if lines[:-1] not in delete_lines and lines[0] != " ":
                f.writelines(lines)
            # print(lines[:-1])
        # landmark.append(lines[:-1])
    










# str1 = "this is string example....wow!!!";
# str2 = "exam";

# print (str1.find(str2))
# print (str1.find(str2, 16))
# print (str1.find(str2, 40))

# str1 = "高雄市那瑪夏區台29線11K+0~23K+0"

# # print(str1.isalnum())
# # print(str1.isalpha())
# # print(str1.isdigit())
# # print(str1.isdecimal())
# # print(str1.isnumeric())

# # word = "台29線"
# # word_find = ["k","K","~","+"]
# # for m in re.finditer("[1234567890kK~+]",str1):
# #     print(m)

# word_find = re.compile("[1234567890kK~+]")
# # match = word_find.finditer(str1,10)
# # for m in match:
# #     print(m)
# match = word_find.finditer(str1,10)

# cnt = 0
# for m in match:
#     if cnt==0:
#         ini = m.start()
#     last_id = m.start()
#     cnt+=1    
#     # print(cnt)
#     if (m.start()-last_id)<=1:
#         end = m.end()
# # print(ini)
# # print(end)
# print(str1[ini:end])


# num = "68K"

# print(int(num[:-1]))