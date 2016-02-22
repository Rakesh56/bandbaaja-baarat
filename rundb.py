import sqlite3
from weather_condition import *
from flask import Flask, jsonify
app = Flask(__name__)
city=raw_input('Enter the city name: ')
locality=raw_input('enter the locality: ')
date=raw_input('Enter the no of days after which u want result <=15 ')
flag=0
conn=sqlite3.connect('adi.db')
cur=conn.cursor()
tasks=[]
tasks.append({"city":{"name":city,"area":locality}})
ma_flag=0
for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality)):
    flag=1 #checking if data exist or not
    break
if flag==0:
    not_in_db(city,locality,date)       
for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality )):
    if ma_flag==0:
        tasks.append({"marriage_lawn/halls":[{"ma_name":row[2],
                        "ma_address":row[3],
                        "ma_contact":row[4]}]})
        ma_flag=1
    else:
        tasks[1]["marriage_lawn/halls"].append({"ma_name":row[2],
                        "ma_address":row[3],
                        "ma_contact":row[4]})
print ('catering one\n\n')
ma_flag=0
for row in cur.execute('SELECT * FROM Mycaters WHERE city=? AND locality=?',(city,locality )):
    if ma_flag==0:
        tasks.append({"marriage_catering":[{"cat_name":row[1],
                        "cat_address":row[3],
                        "cat_contact":row[4]}]})
        ma_flag=1
    else:
        tasks[2]["marriage_catering"].append({"cat_name":row[1],
                        "cat_address":row[3],
                        "cat_contact":row[4]})
print ('tent one\n')
ma_flag=0
for row in cur.execute('SELECT * FROM Mytents WHERE city=? AND locality=?',(city,locality )):
    if ma_flag==0:
        tasks.append({"marriage_tents":[{"tents_name":row[1],
                        "tents_address":row[3],
                        "tents_contact":row[4]}]})
        ma_flag=1
    else:
        tasks[3]["marriage_tents"].append({"tents_name":row[1],
                        "tents_address":row[3],
                        "tents_contact":row[4]})
                                     
@app.route('/todo', methods=['GET'])
def get_tasks():    
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
conn.close()        
