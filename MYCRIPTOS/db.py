import sqlite3
from datetime import date



def Comprar(self):
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    now=datetime.now()
    nowD=now.date()
    nowT=now.time()

    id =["id"]
    print(id)
    date= nowD
    time = nowT
    CurrencyFrom = self.CurrencyFrom.get() 
    Qf = float(self.QFrom.get())
    CurrencyTo = self.CurrencyTo.get()
    CurrencyPurchase = datos["data"]["quote"][CurrencyTo]["price"]
    

    c.execute()
    compras ('INSERT INTO Movements VALUES (?,?,?,?,?,?,?)', id, date, time, CurrencyFrom,Qf,CurrencyTo,CurrencyPurchase)
    conn.commit()

    print(c.fetchall())