from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import requests
from datetime import datetime






from MYCRIPTOS.db import*
from MYCRIPTOS.api import *


parrilla =[
    {
        'text': 'DATE',
        'r': 0,
        'c': 1,
    },
    {
        'text': 'TIME',
        'r': 0,
        'c': 2,
    },
    {
        'text': 'FROM',
        'r': 0,
        'c': 3,

    },
    {
        'text': 'Q',
        'r': 0,
        'c': 4,
    },
    {
        'text': 'TO',
        'r': 0,
        'c': 5,
    },
    {
        'text': 'Q',
        'r': 0,
        'c': 6,
    }
]




class Movimientos(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)    
    
        movimientos = ttk.Frame(self)
        movimientos.pack(side=TOP)
        v1= ttk.Frame(movimientos)
        v1.pack(side=TOP, ipady= 10)
        V11 = ttk.Frame(v1)
        V11.pack(side=BOTTOM, ipady=5)
        lbl_Fecha= ttk.Label(v1, text="Fecha", width= 13).pack(side=LEFT)
        lbl_Hora =ttk.Label(v1, text="Hora", width= 13).pack(side=LEFT)
        lbl_From =ttk.Label(v1, text="From", width= 13).pack(side=LEFT)
        lbl_Q =ttk.Label(v1, text="Q", width= 13).pack(side=LEFT)
        lbl_TO =ttk.Label(v1, text="TO", width= 13).pack(side=LEFT)
        lbl_Q =ttk.Label(v1, text="Q", width= 13).pack(side=LEFT)
        lbl_PU =ttk.Label(v1, text="PU", width= 13).pack(side=LEFT)

        btn= ttk.Button(movimientos, text=" Iniciar", command= self.mostrarDatos)
        btn.pack(side= RIGHT)

        self.tabla = ttk.Label(movimientos, background="white", width=100)
        self.tabla.pack(side=LEFT, ipadx=15, ipady= 15)



    def mostrarDatos(self):


        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()
        c.execute('SELECT   Date, Time, MoneyF, MoneyQ, CurrencyT, CurrencyQ from MOVEMENTS ;')

        resultado= c.fetchall()
        conn.commit()
        conn.close()
        
        for f in resultado:            
            for c in resultado:
        
                m= (f,"\n",c)            
                print(m)
            

        self.tabla.config(text=m)
    


    
            



class Compras(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        compras =ttk.Frame(self)
        compras.pack(side=LEFT)
        FROM= ttk.Frame(compras)
        FROM.pack(side=LEFT, pady= 5)
        Q=ttk.Frame(FROM)
        vcmd= Q.register(self.entrada_permitida) 
        Q.pack(side=BOTTOM, pady= 5)
        nuevasMonedas= self.AñadeMoneda()
        
        
        self.lblFrom = ttk.Label(FROM, text="From: ",  width=5)
        self.lblFrom.pack(side= LEFT, fill= X, padx= 5, pady= 10)
        self.CurrencyFrom= StringVar()   
        self.comboFrom = ttk.Combobox(FROM, values=nuevasMonedas, textvariable= self.CurrencyFrom, state="readonly")
        self.comboFrom.pack(side= LEFT)

        
        self.labelQ = ttk.Label(Q, text="Q:" ,width= 4)
        self.labelQ.pack(side= LEFT, fill= X,  padx= 5, pady= 10)
        self.QFrom= DoubleVar()
        self.entryQFrom = ttk.Entry(Q, textvariable=self.QFrom, width=23, validatecommand=(vcmd,'%S','%P','%s' ), validate="all")
        self.entryQFrom.pack(side=LEFT, fill= X,  padx=5, pady=10)       
        

        compras =ttk.Frame(self)
        compras.pack(side=LEFT)
        TO= ttk.Frame(compras)
        TO.pack(side=LEFT, pady= 5, padx= 60)
        Q =ttk.Frame(TO)
        Q.pack(side=BOTTOM, pady= 5)
        PU = ttk.Frame(Q)
        PU.pack(side=BOTTOM, pady= 5)
        
        self.CurrencyTo= StringVar()
        self.labelTo = ttk.Label(TO,  text="TO : ", width=7)
        self.labelTo.pack(side= LEFT,  padx= 10, pady= 10)
        self.comboTo = ttk.Combobox(TO, values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"),
        textvariable= self.CurrencyTo , state="readonly")
        self.comboTo.pack(side= LEFT)

        self.labelQ = ttk.Label(Q, text="Q:" ,width= 5).pack(side= LEFT,   padx= 10, pady= 10)
        self.QTo=DoubleVar()
        self.labelQTo = ttk.Label(Q, textvariable=self.QTo, width=23, relief= "groove")
        self.labelQTo.pack(side=LEFT,  padx=10, pady=10)
        
        self.labelPU = ttk.Label(PU, text="P.U. : " ,width=5).pack(side= LEFT, padx= 10, pady= 10)
        self.PUnd=DoubleVar()
        self.labelPU = ttk.Label (PU ,textvariable= self.PUnd, width=23, relief= "groove")
        self.labelPU.pack(side=LEFT, padx=10, pady=10) 
        
        compras =ttk.Frame(self)
        compras.pack(side=LEFT)  
        v4= ttk.Frame(compras)
        v4.pack(side=LEFT, padx= 120)
        
        
        ttk.Button(v4,text="Aceptar", command = self.Comprar).pack(side= TOP , pady=5)
        ttk.Button(v4,text="Cancelar").pack(side= TOP,pady= 5)
        ttk.Button(v4,text="Consulta Api", command= self.peticion).pack(side= TOP , pady=5)

    
        
    def entrada_permitida(self,S,P,s):
        
        print("S: ",S, "s: ",s, "P: ",P)


    def peticion(self):
        

        CurrencyF = self.CurrencyFrom.get() 
        Qf = float(self.QFrom.get())
        CurrencyT = self.CurrencyTo.get()
        
       
        CurrencyPurchase = peticion(CurrencyF, Qf, CurrencyT)
        self.QTo.set(CurrencyPurchase)
        PU= round(float(Qf / CurrencyPurchase), 2)
        self.PUnd.set(PU)


            
       

    def Comprar(self):
        
        CurrencyF = self.CurrencyFrom.get() 
        Qf = float(self.QFrom.get())
        CurrencyT = self.CurrencyTo.get()
        CurrencyP = self.QTo.get()
        
        comprar= Comprar(CurrencyF, Qf,CurrencyT,CurrencyP)
       

    def AñadeMoneda(self):
        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()

        c.execute( "SELECT CurrencyT from MOVEMENTS ;")
        monedasBD= c.fetchall()
        conn.commit()
        conn.close()       

        l=["EUR",]

        for m in monedasBD:
            if m[0] != ""  and  m[0] not in l:              
                l.append(m[0])        
        return l

    def EliminaMonedas(self):
        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()

        c.execute( "SELECT CurrencyT , CurrencyQ from MOVEMENTS ;")
        saldoMoneda = c.fetchall()
        conn.commit()
        conn.close()  

        DictMonedas = dict(saldoMoneda)
        cripto= DictMonedas.keys()
        cantidad=DictMonedas.values()

       
        


class Resumen(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        resumen=ttk.Frame(self)
        resumen.pack(side=BOTTOM)
        v5= ttk.Frame(resumen)
        v5.pack(side=BOTTOM, ipady= 10)

        separar=ttk.Separator(v5, orient=HORIZONTAL).pack(side=TOP, padx=5, pady=5)

       
        ttk.Label(v5, text="€ invertidos:", width= 10).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        self.miEUR= ttk.Label(v5, width= 15, relief= "groove")
        self.miEUR.pack(side=LEFT, padx=5, pady=5)

        ttk.Label(v5, text=" Valor actual:", width= 12).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        self.valorAct =ttk.Label(v5, width= 15, relief= "groove")
        self.valorAct.pack(side=LEFT, padx=5, pady=5)

        ttk.Button(v5,text="Calcular", command= self.status ).pack(side= LEFT, fill= X )
        ttk.Button(v5,text="Consultar Saldo", command=self.saldo).pack(side= LEFT, fill= X )
  

    def status(self):

        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()  
        c.execute( "SELECT SUM(MoneyQ) FROM MOVEMENTS WHERE MoneyF ='EUR';")
        miEUR= c.fetchall()    

        c.execute("SELECT MoneyF, MoneyQ FROM MOVEMENTS;")
        sumaFrom= c.fetchall()
        dictFrom={}
        for elements in sumaFrom:
            if elements[0] in dictFrom:
                dictFrom[elements[0]] += elements[1]
            else:
                dictFrom[elements[0]] = elements[1]
        print(dictFrom)
        
        c.execute( "SELECT CurrencyT, CurrencyQ FROM MOVEMENTS;")
        sumaTo=c.fetchall() 
    
        conn.commit()
        conn.close()
       
        self.miEUR.config(text=miEUR)
        
        dictTo=dict(sumaTo)
       
        monedasT=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX")
        l=[]
        m=[]
        
        for monedas in dictFrom:            
            if monedas in dictTo:
                l.append(monedas)
                if monedas in dictFrom:
                    if monedas in dictTo:
                        valorCripto=dictTo[monedas]-dictFrom[monedas]                       
                        m.append(valorCripto)
                        #d =  dict(zip(l,[valorCripto]))     
                        #print(d)  
                
                        #print(monedas)
                        #print(l)
        d=dict(zip(l,m))
        print(d)
        '''
        total=dict()
        for clave,valor in dictFrom.items():
            for clave2, valor2 in dictTo.items():
                if clave== clave2:
                    total[clave]  =  valor -valor2
        print(total)                    
        '''
    def bd(self):
        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()

                
           


              
        

        



        

        

             
        

        
       


            

   



        '''
        url_template = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert=EUR&CMC_PRO_API_KEY=7cbc308d-5a35-45c2-bfe2-c8da53d30f41".format(miValor, CurrencyF,APIkey)
        respuesta = requests.get(url_template)

        if respuesta.status_code == 200:      
            datos = respuesta.json()   
            valor = round(datos["data"]["quote"]["EUR"]["price"], 2)
        '''
        
 

    def saldo(self):
       
        saldo =Toplevel()
        saldo.geometry("700x100")
        saldo.title("Saldo Criptos")
        saldo.grab_set()

        
        self.lblEUR= ttk.Label(saldo,text="Criptos").pack(side=TOP)


        ttk.Label(saldo, text=" saldo en criptos :", width= 15).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)
        self.criptoSaldo=ttk.Label(saldo, width= 70, relief= "groove")
        self.criptoSaldo.pack(side=LEFT, padx=5, pady=5)
   
        conn = sqlite3.connect("MYCRIPTOS/data/base_de_datos.db")
        c = conn.cursor()

        c.execute( "SELECT CurrencyT , CurrencyQ from MOVEMENTS ;")
        criptoSaldo = c.fetchall()
        conn.commit()
        conn.close()  

        for c in criptoSaldo:
            for x in criptoSaldo:
                z=(c,"\n",x)
                print(z)
      
        self.criptoSaldo.config(text=z)
  

        





            


 












        

    
