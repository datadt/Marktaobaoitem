# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author:      datadt
@DateTime:    2018-08-09 11:34:45
'''
#subject:商品图片打标，logo，id，price
#note：原理-位置覆盖，透明图效果极差，不建议使用，白色背景便于优化；
import time
from PIL import Image, ImageDraw, ImageFont
from tbpic import tbpicdl
from tbprice import getprice
from tbshopitemid import gettmallid,getpages
from multiprocessing import Pool


def tiebiao(id):
	tbpicdl(id)
	img = Image.open(str(id)+".jpg")
	jgz = Image.open("logo.jpg")
	img.paste(jgz,(10,10))
	draw = ImageDraw.Draw(img)
	ttfront = ImageFont.truetype('msyh.ttc',25)#自定义字体类型及大小
	draw.text((11, 555),title(id),fill=(255,100,88), font=ttfront)#fill颜色
	img.save('{}.jpg'.format(str(id)))#保存 # img.show()#显示
	print("打标完成！")

def title(id):
	t="ID:"+str(id)+'\n现价: ￥'+getprice(id)+'\n'+time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
	return t

if __name__ == '__main__':
	pool = Pool(processes=5)
	name='huaweistore'#测试
	result=pool.map_async(tiebiao,gettmallid(name,range(1,getpages(name)+1))).get(120)#多进程版
	result.wait()
