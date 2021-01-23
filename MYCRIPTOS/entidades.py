from tkinter import *
from tkinter import ttk





class Movimientos(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.pack_propagate(0)
        
        movimientos = ttk.Frame(self)
        movimientos.pack(side=TOP)
        v1= ttk.Frame(movimientos)
        v1.pack(side=TOP)
    
        ttk.Button(v1,text="Aqui van los movimientos").pack(side= TOP, fill= X )


class Compras(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent,width=700, height=500)
        self.pack_propagate(False)

        compras =ttk.Frame(self)
        compras.pack(side=TOP)
        v2= ttk.Frame(compras)
        v2.pack(side=LEFT)
        
        self.lblFrom = ttk.Label(v2, text="From: ", width=5)
        self.lblFrom.pack(side= TOP, fill= X,  padx= 10, pady= 10)   
        self.comboFrom = ttk.Combobox(v2, values=("EUR"))
        self.comboFrom.pack(side= TOP)

        self.labelQ = ttk.Label(v2, text="Q:" ,width= 5)
        self.labelQ.pack(side= TOP, fill= X,  padx= 10, pady= 10)
        self.Q=DoubleVar()
        self.entryQ = ttk.Entry(v2, textvariable=self.Q, width=23)
        self.entryQ.pack(side=TOP, fill= X,  padx=10, pady=10)

        compras =ttk.Frame(self)
        compras.pack(side=TOP)
        v3= ttk.Frame(compras)
        v3.pack(side=LEFT)
        
        self.labelTo = ttk.Label(v3,  text="TO : ", width=5)
        self.labelTo.pack(side= TOP, fill= X,  padx= 10, pady= 10)
        self.comboTo = ttk.Combobox(v3, values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"))
        self.comboTo.pack(side= TOP)

        self.labelQ = ttk.Label(v3, text="Q:" ,width= 5)
        self.labelQ.pack(side= TOP, fill= X,  padx= 10, pady= 10)
        self.Q=DoubleVar()
        self.entryQ = ttk.Entry(v3 , textvariable=self.Q, width=23)
        self.entryQ.pack(side=TOP, fill= X,  padx=10, pady=10)

        self.labelPU = ttk.Label(v3, text="P.U. : ", width=5)
        self.labelPU.pack(side= TOP, fill= X,  padx= 10, pady= 10)
        self.entryPU = ttk.Entry(v3 , width=23)
        self.entryPU.pack(side=TOP, fill= X,  padx=10, pady=10) 
        compras =ttk.Frame(self)
        compras.pack(side=TOP)  
        v4= ttk.Frame(compras)
        v4.pack(side=LEFT)
        
        ttk.Button(v4,text="Aceptar").pack(side= TOP, fill= X )
        ttk.Button(v4,text="Cancelar").pack(side= TOP, fill= X )
        ttk.Button(v4,text="Consulta Api").pack(side= TOP, fill= X )


class Resumen(ttk.Frame):
    def __init__(self):
        ttk.Frame.__init__(self)
        self.pack_propagate(0)
        resumen=ttk.Frame(self)
        resumen.pack(side=TOP)
        v4= ttk.Frame(resumen)
        v4.pack(side=BOTTOM)

        ttk.Label(v4, text="€ invertidos:", width= 10).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        ttk.Entry(v4, width= 15).pack(side=LEFT, padx=5, pady=5)

        ttk.Label(v4, text=" Valor actual:", width= 10).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        ttk.Entry(v4, width= 15).pack(side=LEFT, padx=5, pady=5)

        ttk.Button(v4,text="Calcular").pack(side= TOP, fill= X )





