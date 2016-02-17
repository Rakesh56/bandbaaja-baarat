import requests
from bs4 import BeautifulSoup
city=raw_input()
url='http://www.matrimonydirectory.com/wedding-venues-in-' +city
r=requests.get(url)
s=BeautifulSoup(r.content)
g=s.find_all("div",{"class":"listing-top clearfix"})
for item in g:
	print item.find_all("p",{"class":"list-heading"})[0].text
	print item.find_all("p",{"class":"list-address list-map-address"})[0].text.replace("| Map"," ")
	print item.find_all("div",{"class":"right-list right-call right-text"})[0].text
	print "\n"