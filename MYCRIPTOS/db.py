import sqlite3
from datetime import datetime
from sqlite3 import Error


def sql_connection():
        try:
            conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
            return conn

        except Error:
            print(Error)


def Comprar(CurrencyF, Qf,CurrencyT,CurrencyP):
    #try:
    conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
    c = conn.cursor()

    now=datetime.now()  
    nowD=now.date()   
    nowT=now.time()

    c.execute('INSERT INTO MOVEMENTS ( Date, Time, MoneyF, MoneyQ, CurrencyT, CurrencyQ ) VALUES (?,?,?,?,?,?);', 
        ( str(nowD), str(nowT), CurrencyF, Qf ,CurrencyT, CurrencyP
        ))
    
        #messagebox.showinfo("correcto")

    #except:
        #messagebox.showwarning("problema conexion")

    conn.commit()
    conn.close()
sql_connection()







