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


import gmplot

gmap = gmplot.GoogleMapPlotter(23.959574,120.5854674, 16)
latitudes = [23.959574, 23.4354677]
longitudes = [120.5854674,120.7809676]

# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(latitudes, longitudes, '#e0190b', size=4000, marker=False)
gmap.scatter(latitudes, longitudes, 'r', marker=True)
# gmap.heatmap(heat_lats, heat_lngs)

gmap.draw("mymap.html")






# highway_pd = Special_words().highway_mark()
# lat = highway_pd.loc[highway_pd['Stake'] == "3K+000"].loc[highway_pd['RoadName'] == "台1線", "latitude"].values[0]
# lon =highway_pd.loc[highway_pd['Stake'] == "3K+000"].loc[highway_pd['RoadName'] == "台1線", "longitude"].values[0]
# coor = [lat,lon]
# print(coor)
# print(type(str(lat)))






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