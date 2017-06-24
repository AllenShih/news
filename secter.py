import requests
from bs4 import BeautifulSoup

url="https://zh.wikipedia.org/wiki/%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E8%87%BA%E7%81%A3%E5%9C%B0%E5%8D%80%E9%84%89%E9%8E%AE%E5%B8%82%E5%8D%80%E5%88%97%E8%A1%A8"

r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,"lxml")

all=soup.find_all("td",{"align":"left"})

sector=[]

for sec in all:
    sect = sec.text.split('、')
    for stat in sect:
        if stat[0] == " ":
            # front = stat[1:-1]
            sector.append(stat[1:])
            # sector.append(front)
        else:
            # front = stat[0:-1]
            sector.append(stat)
            # sector.append(front)

print(sector)
