from tkinter import *
from tkinter import ttk


from MYCRIPTOS import entidades 
from MYCRIPTOS.db import *

class Cripto(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("My Cripto Exchange")
        self.geometry("900x500")
        self.iconbitmap("imagenes/bolsa.ico")

        
        self.movimientos = entidades.Movimientos(self, self.habilitar)
        self.movimientos.pack(side=TOP)
        
       
        self.compras = entidades.Compras(self, self.Comprar)
        self.compras.pack(side=TOP)
        mostrar(self.movimientos.myList)
        
        


        self.resumen = entidades.Resumen(self)
        self.resumen.pack(side=TOP)

    def habilitar(self):    
        self.compras.comboFrom.config(state="readonly")
        self.compras.entryQFrom.config(state="normal")
        self.compras.comboTo.config(state="readonly")
        mostrar(self.movimientos.myList)
        self.compras.comboFrom.config(values= self.compras.AñadeMoneda())
        

    
    def Comprar(self):                
        CurrencyF = self.compras.CurrencyFrom.get() 
        Qf = float(self.compras.QFrom.get())
        CurrencyT = self.compras.CurrencyTo.get()
        CurrencyP = self.compras.QTo.get()
        PU=  Qf/ CurrencyP  


        if CurrencyF != "" :
            self.compras.CurrencyFrom.set("")  
            self.compras.entryQFrom.config(state='normal')               
        else:
            CurrencyF = self.compras.CurrencyFrom.get()

        if Qf != 0 :
            self.compras.QFrom.set(0.0)
        else:
            Qf = float(self.compras.QFrom.get())
        
        if CurrencyT != "":
            self.compras.CurrencyTo.set("")
        else:
            CurrencyT = self.compras.CurrencyTo.get()

        if CurrencyP != "":
            self.compras.QTo.set("")
        else:
            CurrencyP = self.compras.QTo.get() 

        if PU != 0:
            self.compras.PUnd.set(0.0)
        else:
            PU=  Qf/CurrencyP
        
        comprar= Comprar(CurrencyF, Qf,CurrencyT,CurrencyP, PU) 
        self.habilitar()
         
        
    

   


    

    
        
            

if __name__ == "__main__":
    app = Cripto()
    app.mainloop()

