# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@DateTime:    2018-08-08 17:09:03
'''
#subject:获取主图way4

import requests
from bs4 import BeautifulSoup
import urllib.request
import re

def tbpicdl(id,size=800):
	url='https://item.taobao.com/item.htm?id='+str(id)
	soup=BeautifulSoup(requests.get(url).text,'lxml')
	try:
		try:
			try:
				s=soup.find_all('ul',attrs={'id':'J_UlThumb'})[0]#解决颜色等分类描述没有图片的情况，按照第一张预览图取主图 way1
			except:
				s=soup.find_all('img',attrs={'id':'J_ImgBooth'})[0]#取第一张图 way2
		except:
			try:
				s=soup.find_all('dl',attrs={'class':'tb-prop tm-sale-prop tm-clear tm-img-prop '})[0]#列表内元素，链接多商品的情况下取第一个商品图片链接 way3
			except:
				s=soup##直接从网页源获取 way4
		finally:
			pattern=re.compile('//(.*?)_\d+x\d+q90.jpg')
			result=pattern.findall(str(s))[0]
			picurl='https://'+result+'_'+str(size)+'x'+str(size)+'q90.jpg'
			urllib.request.urlretrieve(picurl, "%s.jpg" % str(id))
	except:
		print('Download failed,Try again!',str(id))#采集过快速、过频繁会出错，打印错误ID，可重来
