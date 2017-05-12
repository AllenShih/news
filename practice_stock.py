# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


url='http://www.tse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU.php'

def parseTSE(year, month ,no):
    year=str(year)
    month=str(month)
    no=str(no)
    
    payload = {
        'query_year': year,
        'query_month': month,
        'CO_ID': 2317,
        'query-button':'%E6%9F%A5%E8%A9%A2'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    
    res = requests.post(url, headers=headers, data=payload)
    # data = res.text.encode('latin1').decode('big5')
    # 如果編碼是big5，將會是亂碼，則需先將解碼成latin1再轉成big5
    soup = BeautifulSoup(res.text, 'html.parser')
    
    content = soup.find('table')
    
    # print(str(content))
    
    with open('./'+ year+ month+ '_tse_'+ no +'.html', 'w', encoding = 'utf8') as f:
        f.write(str(content))

    table = pd.read_html('./'+ year+ month+ '_tse_'+ no +'.html', encoding = 'utf8')[0]
    # table = table.drop(table.index[0:1])
    print(table.to_csv(header=False, index=False))

    with open('./'+ year+ '_tse_'+ no +'.csv', 'a', encoding = 'utf8') as f:
        f.write(str(table.to_csv(header=False, index=False)))

for m in range(1,13): #(1,2,3,...,12)
    time.sleep(3)
    parseTSE(2015,m,2317)