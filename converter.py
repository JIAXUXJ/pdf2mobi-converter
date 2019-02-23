# MIT License
# Copyright (c) 2019 Jia

import requests
from bs4 import BeautifulSoup
import pdfkit
from tkinter import *

if __name__ == '__main__':
	# ----------------------gui window begin---------------------- 
	def on_click():  
		label['text'] = 'on click'  

	root= Tk(className='pdf to mobi converter') 
	label = Label(root)  
	label['text'] = 'label text'  
	label.pack() 
	button = Button(root)  
	button['text'] = 'change it'  
	button['command'] = on_click   
	button.pack()  
	root.mainloop()   

	# -----------------------gui window end-----------------------
	# source_type = input("Please select type of your source file:\n1. html link; \n2. pdf file\n")
	# target_type = input("Please select type of target file to convert: \n1. pdf; \n2. mobi\n")
	# # inputlink = input("Please input the link of html page: ")
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


