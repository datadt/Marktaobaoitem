# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@DateTime:    2018-05-30 15:26:47
'''
#获取销售价格

from selenium import webdriver
import requests

def getprice(id):
	co = webdriver.ChromeOptions()
	co.add_argument('--headless')#无壳/头浏览器
	co.add_argument('--User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Safari/537.36')
	co.add_argument('--disable-gpu')
	prefs = {"profile.managed_default_content_settings.images": 2}#禁止加载图片，提升效率
	co.add_experimental_option("prefs", prefs)
	browser = webdriver.Chrome(chrome_options=co)#,desired_capabilities=desired_capabilities

	browser.get('https://detail.tmall.hk/hk/item.htm?id='+str(id))
	PromoPrice = browser.find_element_by_css_selector('#J_PromoPrice > dd > div > span').text#正常促销价
	return PromoPrice
	browser.quit()





#有时候采集不到，需要切换到控制模式下查看执行情况，偶尔登录账号试试
