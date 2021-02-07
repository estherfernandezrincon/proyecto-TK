import sqlite3
from datetime import datetime
from sqlite3 import Error
from MYCRIPTOS.entidades import *
from MYCRIPTOS.tools import config

DBFILE= config ['DBFILE']

def createTabla():
    try:    
        conn = sqlite3.connect(DBFILE)
        c = conn.cursor()
        c.execute( '''CREATE TABLE IF NOT EXISTS MOVEMENTS (
            id INTEGER PRIMARY KEY 
            Date TEXT NOT NULL,
            Time TEXT NOT NULL,
            MoneyF TEXT NOT NULL,
            MoneyQ REAL,
            CurrencyT TEXT NOT NULL,
            CurrencyQ REAL NOT NULL,
            P REAL
        )''')
        print("Tabla creada con exito")
    except Exception as e:
            print( "se ha producido un error en status: {}".format(e))
            self.config(messagebox.showerror(message="error acceso base de datos", title=" ERROR BD"))
    
createTabla()
conn.close()

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








