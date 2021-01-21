from tkinter import *
from tkinter import ttk





class Movimientos(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack_propagate(0)
  

    

class Compras(ttk.Frame):

    def __init__(self, fCenter, frame_one):
        ttk.Frame.__init__(self, fCenter, frame_one)
        self.pack_propagate(0)

        self.label = ttk.Label(self, fCenter, frame_one,text="From: ", width=5)
        self.label.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

        self.combo = ttk.Combobox(self, fCenter, frame_one, values=("EUR"))
        self.combo.pack(self, side= LEFT)
        
        self.label = ttk.Label(self, fCenter, frame_one, width= 5)
        self.label.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

        self.entry = ttk.Entry(self ,fCenter, frame_one,width=23)
        self.entry.pack(side=LEFT, fill= X,  padx=10, pady=10)
        '''

        self.label = ttk.Label(self, fCenter, text="Q : ", width=5)
        self.label.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

        self.combo = ttk.Combobox(self,fCenter,  values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"))
        self.combo.pack(self, side= LEFT)

        self.label = ttk.Label(self, fCenter, text="Q : ", width=5)
        self.label.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

        self.entry = ttk.Entry(self ,fCenter, width=23)
        self.entry.pack(side=LEFT, fill= X,  padx=10, pady=10)  

        self.label = ttk.Label(self, fCenter, text="P.U. : ", width=5)
        self.label.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

        self.entry = ttk.Entry(self ,fCenter, width=23)
        self.entry.pack(side=LEFT, fill= X,  padx=10, pady=10) 

'''


class Resumen(ttk.Frame):
    def __init__(self, Frame):
        ttk.Frame.__init__(self, Frame)
        self.pack_propagate(0)


class Cripto(ttk.Frame):

    def __init__(self, Frame):
        ttk.Frame.__init__(self, Frame)
        self.pack_propagate(0)
 
        self.purchase= Compras(self)
        self.purchase.pack(side=TOP,fill= X, expand= TRUE )