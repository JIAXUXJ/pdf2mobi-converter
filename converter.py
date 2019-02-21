# User: jx
# Date: 2019-02-20
import requests
from bs4 import BeautifulSoup
import pdfkit

if __name__ == '__main__':
	# inputlink = input("Please input the link of html page: ")
	# hardcode of link:
	inputlink = "http://python3-cookbook.readthedocs.io/zh_CN/latest/"
	wb = requests.get(inputlink)
	wb.encoding = "utf-8"

	urls = []

	if wb.ok:
		soup = BeautifulSoup(wb.text,'html.parser')
		print(soup.prettify())

