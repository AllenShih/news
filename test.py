#!/usr/bin/env python3
import re

with open("臺灣省道編號座標.csv", encoding = 'utf8') as w:
    f= open("highway_mark.csv", "w", encoding = 'utf8')
    content = w.readlines()
    cnt = 0
    for lines in content:
        if cnt == 0:
            f.writelines(lines)
            cnt += 1
        else:
            new_line = lines.split(",")
            k_part = new_line[0].split("+")
            num_part = k_part[0][:-1]
            new_kpart = str(int(num_part))+"K"
            new_0 = new_kpart + "+" + k_part[1]
            new_line[0] = new_0
            new_line_ = ",".join(new_line)
            f.writelines(new_line_)


# word = "0014"
# print(eval(word))





















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





