# MIT License
# Copyright (c) 2019 Jia

import tkinter as tk
from tkinter import filedialog


class Guiwindow(object):
	"""docstring for Guiwindow"""
	def __init__(self):
		super(Guiwindow, self).__init__()
		# ----------------------gui window begin---------------------- 
		window = tk.Tk()  
		window.title("pdf2mobi converter")
		window.geometry("700x400")
		window.configure(background="#FFFFF0")

		file_var = tk.StringVar()

		def callback():
			fileName = filedialog.askopenfilename()
			file_var.set("File to convert: "+fileName)
		upload_b = tk.Button(window,text='Open a pdf file', command=callback)
		upload_b.config(highlightbackground = "#FFFFF0")
		upload_b.pack(fill = tk.X, padx=250, pady=(20,0))

		file_N = tk.Label(window, textvariable = file_var, bg='#FFFFF0', fg="black")
		file_N.pack(pady=10)

		btn_text = tk.StringVar()
		on_hit = False
		def pdf2mobi():
			global on_hit
			if on_hit == False:
				on_hit = True
				btn_text.set('converting')
		convert_b = tk.Button(window,textvariable=btn_text,command=pdf2mobi)
		btn_text.set("convert to MOBI")
		convert_b.pack(fill=tk.X, padx=250, pady=10)

		window.mainloop()
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

Guiwindow()


