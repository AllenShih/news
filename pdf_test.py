#!/usr/bin/env python3
# -*- coding: utf8 -*-


import requests
from bs4 import BeautifulSoup

# res = requests.get("https://news.google.com")
# soup = BeautifulSoup(res.content,"lxml")
# # print (soup.select(".esc-body"))
# count = 1

# for item in soup.select(".esc-body"):
#     print ('======[',count,']=========')
#     news_title = item.select(".esc-lead-article-title")[0].text
#     news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
#     print (news_title)
#     print (news_url)
#     count += 1

# url = "https://www.google.com/search?q=土石流+pdf"
# res = requests.get(url)
# soup = BeautifulSoup(res.content, "lxml")

# count = 1
# for item in soup.find_all("div",{"class":"g"}):
#     print ('======[',count,']=========')
#     print(item)
#     # news_title = item.select(".esc-lead-article-title")[0].text
#     # news_url = item.select(".esc-lead-article-title")[0].find('a')['href']
#     # print (news_title)
#     # print (news_url)
#     count += 1



from urllib.request import urlopen


def main():
    download_file("http://www.cswcs.org.tw/AllDataPos/JournalPos/VOL44/NO2/jcswc44(2)165-178_07.pdf")

def download_file(download_url):
    response = urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()

