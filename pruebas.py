import sqlite3

conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
c = conn.cursor()

c.execute( "SELECT SUM(MoneyQ) FROM MOVEMENTS WHERE MoneyF ='EUR';")
miEUR= c.fetchall() 

print(miEUR) 

c.execute("SELECT MoneyF, MoneyQ FROM MOVEMENTS;")
nuevaSuma= c.fetchall()

print(nuevaSuma)

c.execute( "SELECT CurrencyT, CurrencyQ FROM MOVEMENTS;")
nuevaS= c.fetchall()
print(nuevaS)


