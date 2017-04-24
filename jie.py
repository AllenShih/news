import jieba
import requests
from bs4 import BeautifulSoup

url="http://www.appledaily.com.tw/realtimenews/article/new/20150927/700101/"
r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,"lxml")

all=soup.find_all("div",{"class":"articulum trans"})

text=all[0].text

seglist = jieba.cut(text, cut_all=False)

for item in seglist:
    print(item)
