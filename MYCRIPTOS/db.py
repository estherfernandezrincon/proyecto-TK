import sqlite3



def Movimientos():
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    c.execute('SELECT Date, Time,From,Q,To,P.U. FROM MOVEMENTS;')
    conn.commit()

    print(c.fetchall())