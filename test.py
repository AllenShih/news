#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import gmplot
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


# delete_lines = ["山區" ,"中央氣象局","日月潭","公路總局","消防局","省道","活動中心","農委會","停車場","水閘","水利","冷泉","教育部","球場","公園","籃球場" ,"水利署","水系","營建署","經濟部","農糧署","交通部","國道","地下停車場","\""]
# print(delete_lines)
# with open("landmark_new_.csv", encoding = 'utf8') as w:
#     with open("landmark_new_2.csv", "w", encoding="utf8") as f:
#         content = w.readlines()
#         for lines in content:
#             if lines[:-1] not in delete_lines and lines[0] != " ":
#                 f.writelines(lines)
#             # print(lines[:-1])
#         # landmark.append(lines[:-1])

highway_coor_lat = [24.251491000000001, 24.195640000000001, 23.159483999999999, 23.216488000000002, 23.159483999999999, 23.216488000000002, 24.251491000000001, 24.195640000000001, 23.569887999999999, 24.029285000000002, 24.195640000000001, 24.251491000000001, 24.023800000000001, 23.159483999999999, 23.216488000000002, 23.569887999999999, 24.035654999999998, 23.813020999999999,
                    23.179205, 24.251491000000001, 24.195640000000001, 23.159483999999999, 23.216488000000002, 23.159483999999999, 23.216488000000002, 24.251491000000001, 24.195640000000001, 23.569887999999999, 24.029285000000002, 24.195640000000001, 24.251491000000001, 24.023800000000001, 23.159483999999999, 23.216488000000002, 23.569887999999999, 24.035654999999998, 23.813020999999999, 23.179205]
highway_coor_lon = [121.16924299999999, 121.30365500000001, 120.75933700000002, 121.01954099999999, 120.75933700000002, 121.01954099999999, 121.16924299999999, 121.30365500000001, 120.89231200000002, 121.17594099999999, 121.30365500000001, 121.16924299999999, 121.18070700000001, 120.75933700000002, 121.01954099999999, 120.89231200000002, 121.185975, 120.850477, 120.78046999999999,
                    121.16924299999999, 121.30365500000001, 120.75933700000002, 121.01954099999999, 120.75933700000002, 121.01954099999999, 121.16924299999999, 121.30365500000001, 120.89231200000002, 121.17594099999999, 121.30365500000001, 121.16924299999999, 121.18070700000001, 120.75933700000002, 121.01954099999999, 120.89231200000002, 121.185975, 120.850477, 120.78046999999999]


gmap = gmplot.GoogleMapPlotter(23.97565,120.973881944444, 6)
latitudes = highway_coor_lat
longitudes = highway_coor_lon
# latitudes = [24.251491000000001, 24.195640000000001]
# longitudes = [121.16924299999999, 121.30365500000001]
# gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
# gmap.scatter(latitudes, longitudes, '#FF6666', marker=True)
gmap.scatter(latitudes, longitudes, '#FF6666', size=4000, marker=False)
# gmap.scatter(latitudes, longitudes, 'r', marker=True)
# gmap.heatmap(latitudes, longitudes)
gmap.draw("new_map.html")




# 123






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
