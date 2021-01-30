from tkinter import *
from tkinter import ttk


from MYCRIPTOS import entidades


class Cripto(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("My Cripto Exchange")
        self.geometry("900x300")
        self.iconbitmap("imagenes/bolsa.ico")


        self.movimientos = entidades.Movimientos(self)
        self.movimientos.pack(side=TOP)
        
        self.compras = entidades.Compras(self)
        self.compras.pack(side=TOP)
        #self.compras.AñadeMoneda()
    

        self.resumen = entidades.Resumen(self)
        self.resumen.pack(side=TOP)
        #self.resumen.CalcularSaldo()
    



if __name__ == "__main__":
    app = Cripto()
    app.mainloop()

