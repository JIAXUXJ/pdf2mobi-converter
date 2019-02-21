# User: jx
# Date: 2019-02-20
import requests
from bs4 import BeautifulSoup
import pdfkit

if __name__ == '__main__':
	source_type = input("Please select type of your source file:\n1. html link; \n2. pdf file\n")
	target_type = input("Please select type of target file to convert: \n1. pdf; \n2. mobi\n")
	# inputlink = input("Please input the link of html page: ")
	# hardcode of link:
	inputlink = "http://python3-cookbook.readthedocs.io/zh_CN/latest/"
	wb = requests.get(inputlink)
	wb.encoding = "utf-8"

	urls = []

	if wb.ok:
		soup = BeautifulSoup(wb.text,'html.parser')
		print(soup.prettify())

