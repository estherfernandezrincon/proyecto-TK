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
       
        self.compras = entidades.Compras(self)
        self.compras.pack(side=TOP)
        mostrar(self.movimientos.myList)

        self.resumen = entidades.Resumen(self)
        self.resumen.pack(side=TOP)

    def habilitar(self):    
        self.compras.comboFrom.config(state="readonly")
        self.compras.entryQFrom.config(state="normal")
        self.compras.comboTo.config(state="readonly")
        mostrar(self.movimientos.myList)

     
            

if __name__ == "__main__":
    app = Cripto()
    app.mainloop()

