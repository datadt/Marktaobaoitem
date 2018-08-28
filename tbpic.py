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
		url='https://item.taobao.com/item.htm?id='+str(id)
		soup=BeautifulSoup(requests.get(url).text,'lxml')
		try:
			s=soup.find_all('dl',attrs={'class':'tb-prop tm-sale-prop tm-clear tm-img-prop '})[0]#列表内元素
			pattern=re.compile('//(.*?)_40x40q90.jpg')
			result=pattern.findall(str(s))[0]#链接多商品的情况下取第一个商品图片链接
			picurl='https://'+result+'_800x800q90.jpg'
		except:
			s=soup.find_all('img',attrs={'id':'J_ImgBooth'})[0]#解决颜色等分类描述没有图片的情况，按照第一张预览图取主图#575745472218
			pattern=re.compile('//(.*?)_430x430q90.jpg')
			result=pattern.findall(str(s))[0]
			picurl='https://'+result+'_800x800q90.jpg'
		finally:
			urllib.request.urlretrieve(picurl, "%s.jpg" % str(id))

