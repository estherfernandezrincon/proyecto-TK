import sqlite3
from datetime import datetime
from sqlite3 import Error
from MYCRIPTOS.entidades import *
from MYCRIPTOS.tools import config

DBFILE= config ['DBFILE']


'''
def sql_connection():
    try:
        conn = sqlite3.connect(config['DBFILE'])
        return conn

    except Error:
        print(Error)
'''

def Comprar(CurrencyF, Qf,CurrencyT,CurrencyP):

    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    now=datetime.now()  
    nowD=now.date()   
    nowT=now.time()

    c.execute('INSERT INTO MOVEMENTS ( Date, Time, MoneyF, MoneyQ, CurrencyT, CurrencyQ ) VALUES (?,?,?,?,?,?);', 
        ( str(nowD), str(nowT), CurrencyF, Qf ,CurrencyT, CurrencyP
        ))
    


    conn.commit()
    conn.close()
#sql_connection()







