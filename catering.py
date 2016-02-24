import requests
from bs4 import BeautifulSoup
import sqlite3
#This below Function will give you data about various catering services available in your city
def caters(city,locality): #web scraping is done to fetch data for caters using beautiful soup
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    url='http://yellowpages.sulekha.com/catering-services_'+city
    r=requests.get(url)
    s=BeautifulSoup(r.content)
    g=s.find_all("li",{"itemtype":"http://schema.org/LocalBusiness"})
    for item in g:
        try:
            #catering service name
            a=item.find_all("a",{"class":"YPTRACK GAQ_C_BUSL"})[0].text
            #catering service contact number
            b=item.find_all("b",{"class":"contact-number"})[0].text
        except:
            pass
        try:
            #catering service address
            c=item.find_all("address",{"class":"pull-left"})[0].text
        except:
            pass
        #inserting info in database
        cur.execute('INSERT INTO Mycaters(city,cater_name,locality,contact_cater,address_cater) VALUES(?,?,?,?,?)',(city,a,locality,b,c))
        conn.commit()
    conn.close()    
