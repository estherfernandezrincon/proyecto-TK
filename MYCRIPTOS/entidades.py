from tkinter import *
from tkinter import ttk





class Movimientos(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        movimientos = ttk.Frame(self)
        movimientos.pack(side=TOP)
        v1= ttk.Frame(movimientos)
        v1.pack(side=TOP, ipady= 10)
        V11 = ttk.Frame(v1)
        V11.pack(side=BOTTOM, ipady=5)

        lbl_Fecha= ttk.Label(v1, text="Fecha", width= 8).pack(side=LEFT)
        lbl_Hora =ttk.Label(v1, text="Hora", width= 8).pack(side=LEFT)
        lbl_From =ttk.Label(v1, text="From", width= 8).pack(side=LEFT)
        lbl_Q =ttk.Label(v1, text="Q", width= 5).pack(side=LEFT)
        lbl_TO =ttk.Label(v1, text="TO", width= 5).pack(side=LEFT)
        lbl_Q =ttk.Label(v1, text="Q", width= 5).pack(side=LEFT)
        lbl_PU =ttk.Label(v1, text="PU", width= 5).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="gray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="lightgray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="gray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="lightgray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="gray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="lightgray", anchor="e", width= 6).pack(side=LEFT)
        ttk.Label(V11,textvariable=self.Consulta, background="gray", anchor="e", width= 6).pack(side=LEFT)
    def Consulta(self):
        pass


class Compras(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        compras =ttk.Frame(self)
        compras.pack(side=LEFT)
        FROM= ttk.Frame(compras)
        FROM.pack(side=LEFT, pady= 5)
        Q=ttk.Frame(FROM)
        Q.pack(side=BOTTOM, pady= 5)
        
        self.lblFrom = ttk.Label(FROM, text="From: ", width=5)
        self.lblFrom.pack(side= LEFT, fill= X, padx= 5, pady= 10)   
        self.comboFrom = ttk.Combobox(FROM, values=("EUR"))
        self.comboFrom.pack(side= LEFT)

        self.labelQ = ttk.Label(Q, text="Q:" ,width= 4)
        self.labelQ.pack(side= LEFT, fill= X,  padx= 5, pady= 10)
        self.Q=DoubleVar()
        self.entryQ = ttk.Entry(Q, textvariable=self.Q, width=23)
        self.entryQ.pack(side=LEFT, fill= X,  padx=5, pady=10)

        compras =ttk.Frame(self)
        compras.pack(side=LEFT)
        TO= ttk.Frame(compras)
        TO.pack(side=LEFT, pady= 5, padx= 60)
        Q =ttk.Frame(TO)
        Q.pack(side=BOTTOM, pady= 5)
        PU = ttk.Frame(Q)
        PU.pack(side=BOTTOM, pady= 5)
        
        self.labelTo = ttk.Label(TO,  text="TO : ", width=7)
        self.labelTo.pack(side= LEFT,  padx= 10, pady= 10)
        self.comboTo = ttk.Combobox(TO, values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"))
        self.comboTo.pack(side= LEFT)

        self.labelQ = ttk.Label(Q, text="Q:" ,width= 5)
        self.labelQ.pack(side= LEFT,   padx= 10, pady= 10)
        self.Q=DoubleVar()
        self.entryQ = ttk.Entry(Q, textvariable=self.Q, width=23)
        self.entryQ.pack(side=LEFT,  padx=10, pady=10)

        self.labelPU = ttk.Label(PU, text="P.U. : ", width=5)
        self.labelPU.pack(side= LEFT,   padx= 10, pady= 10)
        self.PU=DoubleVar()
        self.entryPU = ttk.Entry(PU ,textvariable=self.PU, width=23)
        self.entryPU.pack(side=LEFT,   padx=10, pady=10) 

        compras =ttk.Frame(self)
        compras.pack(side=LEFT)  
        v4= ttk.Frame(compras)
        v4.pack(side=LEFT, padx= 120)
        
        ttk.Button(v4,text="Aceptar").pack(side= TOP , pady=5)
        ttk.Button(v4,text="Cancelar").pack(side= TOP,pady= 5)
        ttk.Button(v4,text="Consulta Api").pack(side= TOP , pady=5)
        


class Resumen(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        resumen=ttk.Frame(self)
        resumen.pack(side=BOTTOM)
        v5= ttk.Frame(resumen)
        v5.pack(side=BOTTOM, ipady= 10)



        separar=ttk.Separator(v5, orient=HORIZONTAL).pack(side=TOP, padx=5, pady=5)

        ttk.Label(v5, text="€ invertidos:", width= 10).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        ttk.Entry(v5, width= 15).pack(side=LEFT, padx=5, pady=5)

        ttk.Label(v5, text=" Valor actual:", width= 12).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        ttk.Entry(v5, width= 15).pack(side=LEFT, padx=5, pady=5)

        ttk.Button(v5,text="Calcular").pack(side= LEFT, fill= X )
        ttk.Button(v5,text="Consultar Saldo", command=self.Saldo,).pack(side= LEFT, fill= X )


    def Saldo(self):
        saldo =Toplevel()
        saldo.geometry("400x100")
        saldo.title("Saldo Criptos")
        saldo.grab_set()
        
        lblEUR= ttk.Label(saldo,text="EUR y Criptos").pack(side=TOP)

        

