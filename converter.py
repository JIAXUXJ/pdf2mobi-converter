# MIT License
# Copyright (c) 2019 Jia

import requests
from bs4 import BeautifulSoup
import pdfkit
import tkinter as TK

if __name__ == '__main__':
	# ----------------------gui window begin---------------------- 
	window = tk.TK()  
	window.title("pdf2mobi converter")
	# -----------------------gui window end-----------------------
	# # hardcode of link:
	# inputlink = "http://python3-cookbook.readthedocs.io/zh_CN/latest/"
	# wb = requests.get(inputlink)
	# wb.encoding = "utf-8"

	# urls = []

	# if wb.ok:
	# 	soup = BeautifulSoup(wb.text,'html.parser')
	# 	# print(soup.prettify())
	# 	div = soup.select('.toctree-l2')
	# 	for i in div:
	# 		each_url = i.contents[0]['href']
	# 		if '#' in each_url:
 #            if each_url.split('#')[0] not in all_urls:
 #                all_urls.append(each_url.split('#')[0])
 #        else:
 #            all_urls.append(each_url)


