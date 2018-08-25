# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@DateTime:    2018-08-08 17:09:03
'''
#subject:获取主图way2


import requests
from bs4 import BeautifulSoup
import urllib.request
import re

def tbpicdl(ids):
	for id in ids:
		url='https://detail.tmall.hk/hk/item.htm?id='+str(id)
		soup=BeautifulSoup(requests.get(url).text,'lxml')
		s=soup.find_all('dl',attrs={'class':'tb-prop tm-sale-prop tm-clear tm-img-prop '})[0]#列表内元素
		pattern=re.compile('//(.*?)_40x40q90.jpg')
		result=pattern.findall(str(s))[0]#链接多商品的情况下取第一个商品图片链接
		picurl='https://'+result+'_800x800q90.jpg'
		urllib.request.urlretrieve(picurl, "%s.jpg" % str(id))

