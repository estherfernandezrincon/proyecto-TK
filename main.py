from tkinter import *
from tkinter import ttk

from MYCRIPTOS import entidades

class Cripto(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("My Cripto Exchange")

        self.Movimientos = entidades.Movimientos(self)
        self.Movimientos.pack(side=TOP)
        
        self.compras = entidades.Compras(self)
        self.compras.pack(side=TOP)

        #self.Resumen = entidades.Resumen(self)
        #self.Resumen.pack(side=TOP)



if __name__ == "__main__":
    app = Cripto()
    app.mainloop()