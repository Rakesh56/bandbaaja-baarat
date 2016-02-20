import requests
from bs4 import BeautifulSoup

def tent(city):
   url='http://yellowpages.sulekha.com/tents-tarpaulin-suppliers-rentals_'+city
   r=requests.get(url) #web scraping is done for tents data using beautiful soup
   s=BeautifulSoup(r.content)
   k=s.find_all("li",{"class":"list-item"})
   for item in k:
      try:
         print item.find_all("a",{"class":"YPTRACK GAQ_C_BUSL"})[0].text
      except:
         pass
      try:
         print item.find_all("b",{"class":"contact-number"})[0].text
      except:
         pass
      try:
         print item.find_all("address",{"class":"pull-left"})[0].text
      except:
         pass
      print "\n"
