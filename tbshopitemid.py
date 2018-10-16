# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@Tool:        Sublime Text3
'''

import requests
import json
import random
import re
import time
import urllib.request

#获取店铺商品信息
def gettmallid(name,pages):
    headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"}
    productid=[]
    productprice=[]
    for page in pages:
        num = random.randint(5376000,5379999)#(87977710,87977810)
        url = 'https://'+name+'.m.tmall.com/shop/shop_auction_search.do?sort=d&p='+str(page)+'&page_size=12&from=h5&ajson=1&_tm_source=tmallsearch&callback=jsonp_'+str(num)
        html = requests.get(url, headers=headers).text
        infos = re.findall('jsonp_\d+\(({.*?})\)', html)[0]
        infos = json.loads(infos)['items']
        for i in infos: #字段 'item_id', 'title', 'img', 'sold', 'quantity','totalSoldQuantity', 'url', 'price','titleUnderIconList' 等
            productid.append(str(i['item_id']))# print(str(i['item_id']))
            productprice.append(str(i['price']))
        time.sleep(abs(random.random()-0.5))
    return productid

#获取页码总数
def getpages(name):
    num = random.randint(5376000,5379999)
    url = 'https://'+name+'.m.tmall.com/shop/shop_auction_search.do?sort=d&p=1&page_size=12&from=h5&ajson=1&_tm_source=tmallsearch&callback=jsonp_'+str(num)
    html = requests.get(url).text
    p1=re.findall('"total_page":"[0-9]{1,}"',html)[0]
    return int(re.findall('[0-9]{1,}',p1)[0])#获取最大页数
