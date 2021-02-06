import sqlite3
from datetime import datetime
from sqlite3 import Error
from MYCRIPTOS.entidades import *
from MYCRIPTOS.tools import config

DBFILE= config ['DBFILE']





def Comprar(CurrencyF, Qf,CurrencyT,CurrencyP,PU):
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    now=datetime.now()  
    nowD=now.date()   
    nowT=now.time()

    c.execute('INSERT INTO MOVEMENTS ( Date, Time, MoneyF, MoneyQ, CurrencyT, CurrencyQ ,P ) VALUES (?,?,?,?,?,?,?);', 
        ( str(nowD), str(nowT), CurrencyF, Qf ,CurrencyT, CurrencyP ,PU 
        ))
    


    conn.commit()
    conn.close()








