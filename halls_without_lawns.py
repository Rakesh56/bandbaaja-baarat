import requests
import collections
from bs4 import BeautifulSoup
from distance import *  #distance apiused in this file
from catering import *
from tents import *

def without_lawns(city,current_add):
    url1='http://yellowpages.sulekha.com/marriage-halls-rentals_'+city
    s=requests.get(url1)
    soup=BeautifulSoup(s.content)
    ob1=soup.find_all('li',{"itemtype":"http://schema.org/LocalBusiness","class":"list-item"})
    i=0
    j=0
    x=()
    arr=[]
    for link in ob1:
        i=0
        string=link.find_all("a",{"itemprop":"url"})[0].text
        try:
            while i<len(string):
                if string[i]==',':
                    break
                i=i+1        
            str2=string[i+2:] #distancematrix api is used to know the distance bt ur locality & hall
            di=finddistance(current_add,city,str2).replace(' km','')
            x=(float(di),link)
            arr.append(x)
        except:
            pass
    arr.sort()    
    for ob1 in arr:
        try:
            print ob1[0]
        except:
            pass
        try:
            print ob1[1].find_all("a",{"itemprop":"url"})[0].text
        except:
            pass
        try:
            print ob1[1].find_all("b",{"class":"contact-number"})[0].text
        except:
            pass
        try:
            print ob1[1].find_all("address",{"class":"pull-left"})[0].text.replace('Get Directions','         ')
        except:
            pass
        print '\n'
                
    print ('CATERING WALAS: ')
    caters(city)
    print ('TENTS WALAS: ')
    tent(city)
