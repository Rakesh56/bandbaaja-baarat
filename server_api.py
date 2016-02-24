import sqlite3
from weather_condition import *
from flask import Flask, jsonify
import uuid
app = Flask(__name__)

@app.route('/get_key/')
def get_newtasks():
    uid=uuid.uuid4()
    api_key=uid.hex
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO takekey(key,key2) Values (?,?)',(api_key,1))
    conn.commit()
    conn.close()
    return ("your  api key is  "+api_key)
    


    
@app.route('/bandbaaja-baarat/city=<string:city>/locality=<string:locality>/api_key=<string:key>/day=<string:date>', methods=['GET'])
def get_tasks(city,locality,key,date):
    #city=raw_input('Enter the city name: ')
    #locality=raw_input('enter the locality: ')
    #date=raw_input('Enter the no of days after which u want result <=15 ')
    flag=0
    flag2=0
    conn=sqlite3.connect('adi.db')
    cur=conn.cursor()
    for row in cur.execute("SELECT  * FROM takekey WHERE key=? AND key2=?",(key,1)):
        flag2=1
        break
    if flag2==1:
        tasks=[]
        tasks.append({"city":{"name":city,"area":locality}})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality)):
            flag=1
            break
        if flag==0:
            not_in_db(city,locality,date)       
        for row in cur.execute('SELECT * FROM Myhalls WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0:
                tasks.append({"marriage_lawn/halls":[{"ma_name":row[2],
                            "ma_address":row[4],
                            "ma_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[1]["marriage_lawn/halls"].append({"ma_name":row[2],
                        "ma_address":row[4],
                        "ma_contact":row[3]})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Mycaters WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0:
                tasks.append({"marriage_catering":[{"cat_name":row[1],
                        "cat_address":row[4],
                        "cat_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[2]["marriage_catering"].append({"cat_name":row[1],
                        "cat_address":row[4],
                        "cat_contact":row[3]})
        ma_flag=0
        for row in cur.execute('SELECT * FROM Mytents WHERE city=? AND locality=?',(city,locality )):
            if ma_flag==0:
                tasks.append({"marriage_tents":[{"tents_name":row[1],
                        "tents_address":row[4],
                        "tents_contact":row[3]}]})
                ma_flag=1
            else:
                tasks[3]["marriage_tents"].append({"tents_name":row[1],
                        "tents_address":row[4],
                        "tents_contact":row[3]})
        return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True,port=963)
conn.close()        
