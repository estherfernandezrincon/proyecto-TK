from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import requests
from datetime import datetime
from configparser import ConfigParser





c= ConfigParser()
c.read('MYCRIPTOS/config.ini')
config = c ['DEFAULT']

DBFILE= config ['DBFILE']
APIkey= config ['APIkey']

class Movimientos(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)   
        
    
        movimientos = ttk.Frame(self)
        movimientos.pack(side=TOP)
        

        cabecera= "Fecha       Hora      From       Q       TO       Q        P.U. "
        fontC= ("Helvetica", 11, "bold")
        fontL= ("Helvetica", 11)
        

        btnReset = ttk.Button(movimientos, text="Reset").pack(side=RIGHT)
        lbl_ppal= ttk.Label(movimientos, font=fontC,text= cabecera ,width= 100, anchor=CENTER)
        lbl_ppal.pack(side=TOP)

        separar=ttk.Separator(movimientos, orient=HORIZONTAL)
        separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
 
        scroll= Scrollbar(movimientos, orient= VERTICAL)
        scroll.pack(side= RIGHT, fill=Y)

        myList= Listbox(movimientos, yscrollcommand= scroll.set, bd=0, font=fontL)
        myList.pack(side=LEFT,fill=BOTH, expand=True)
      

        scroll.config(command=myList.yview)

        try:
            conn = sqlite3.connect(DBFILE)
            c = conn.cursor()
            c.execute('SELECT   Date, Time, MoneyF, MoneyQ , CurrencyT, CurrencyQ from MOVEMENTS ;')

            resultado= c.fetchall()
            conn.commit()
            conn.close()
        except Exception as e:
            print( "se ha producido un error en status: {}".format(e))
            self.config(messagebox.showerror(message="error acceso base de datos", title=" ERROR BD"))            

        for i in resultado:
            myList.insert(END, i)
           


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

        separar=ttk.Separator(FROM, orient=HORIZONTAL)
        separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        lblNT= ttk.Label(FROM, text="NUEVA TRANSACCION", width= 25)
        lblNT.pack(side=TOP)        
        
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
        values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX")
        
        self.CurrencyTo= StringVar()
        self.labelTo = ttk.Label(TO,  text="TO : ", width=7)
        self.labelTo.pack(side= LEFT,  padx= 10, pady= 10)
        self.comboTo = ttk.Combobox(TO, values= values,textvariable= self.CurrencyTo , state="readonly")
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
        
        btnA =ttk.Button(v4,text="Aceptar",command = self.Comprar).pack(side= TOP , pady=5)
        btnCxl= ttk.Button(v4,text="Cancelar", state= "DISABLED",command=self.cancelar).pack(side= TOP,pady= 5)
        btnC=ttk.Button(v4,text="Consulta Api",command= self.peticion).pack(side= TOP , pady=5)

    def cancelar(self):
        if self.CurrencyFrom != "" :
            btnCxl['state'] = NORMAL
            
        
    def entrada_permitida(self,S,P,s):
        
        print("S: ",S, "s: ",s, "P: ",P)


    def peticion(self):
        try:
            CurrencyF = self.CurrencyFrom.get() 
            Qf = float(self.QFrom.get())
            CurrencyT = self.CurrencyTo.get()            
        
            CurrencyPurchase = peticion(CurrencyF, Qf, CurrencyT)
            print(CurrencyPurchase)
        except Exception as e:
            print("error en api: {}".format(e))
            self.config(messagebox.showinfo(message="Se ha producido un error en la API, intentalo más tarde", title="API"))
            return 

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
        try:
            conn = sqlite3.connect(DBFILE)
            c = conn.cursor()

            c.execute( "SELECT CurrencyT from MOVEMENTS ;")
            monedasBD= c.fetchall()
            conn.commit()
            conn.close()   
        except Exception as e:
            print( "se ha producido un error en status: {}".format(e))
            self.config(messagebox.showerror(message="error acceso base de datos", title=" ERROR BD"))            
    

        l=["EUR",]

        for m in monedasBD:
            if m[0] != ""  and  m[0] not in l:              
                l.append(m[0])        
        return l

       
        


class Resumen(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        resumen=ttk.Frame(self)
        resumen.pack(side=BOTTOM)
        v5= ttk.Frame(resumen)
        v5.pack(side=BOTTOM, ipady= 10)



       
        ttk.Label(v5, text="€ invertidos:", width= 10).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        self.miEUR= ttk.Label(v5, width= 15, relief= "groove")
        self.miEUR.pack(side=LEFT, padx=5, pady=5)
        

        ttk.Label(v5, text=" Valor actual:", width= 12).pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)       
        self.valorAct =ttk.Label(v5, width= 15, relief= "groove")
        self.valorAct.pack(side=LEFT, padx=5, pady=5)

        ttk.Button(v5,text="Calcular", command= self.status).pack(side= LEFT, fill= X )
        ttk.Button(v5,text="Consultar Saldo", command=self.saldo).pack(side= LEFT, fill= X )
  

    def status(self):
        try:
            conn = sqlite3.connect(DBFILE)
            c = conn.cursor()  
            c.execute( "SELECT SUM(MoneyQ) FROM MOVEMENTS WHERE MoneyF ='EUR';")
            miEUR= c.fetchall()  
            self.miEUR.config(text=miEUR)  

            c.execute("SELECT MoneyF, MoneyQ FROM MOVEMENTS;")
            sumaFrom= c.fetchall()
            dictFrom={}            
        
            for elements in sumaFrom:
                if elements[0] in dictFrom:
                    dictFrom[elements[0]] += elements[1]
                else:
                    dictFrom[elements[0]] = elements[1]
            
            c.execute( "SELECT CurrencyT, CurrencyQ FROM MOVEMENTS;")
            sumaTo=c.fetchall() 
            dictTo={}

            for elements in sumaTo:
                if elements[0] in dictTo:
                    dictTo[elements[0]] += elements[1]
                else:
                    dictTo[elements[0]] = elements[1]
    
            conn.commit()
            conn.close()
        except Exception as e :
            print( "se ha producido un error en status: {}".format(e))
            self.config(messagebox.showerror(message="error acceso base de datos", title=" ERROR BD"))

      
        l=[]
        m=[]
        
        for monedas in dictFrom:            
            if monedas in dictTo:
                l.append(monedas)
                if monedas in dictFrom:
                    if monedas in dictTo:
                        valorCripto=dictTo[monedas]-dictFrom[monedas]                       
                        m.append(valorCripto)                   
                        
        d=dict(zip(l,m)) 

        amount=[]
        symbol=[]
        a=[]        
        if 'EUR' in d:
            del d['EUR']       
        
        valorAct=[]
        for k,v in d.items():
            cripto= k
            cantidad= v
        try:
            url_template="https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert=EUR&CMC_PRO_API_KEY={}".format(cantidad, cripto, APIkey)
            respuesta = requests.get(url_template)
            if respuesta.status_code == 200:      
                datos = respuesta.json() 
                valor= round(datos["data"]["quote"]["EUR"]["price"], 2)
                valorAct.append(valor)
      
        except Exception as e:
            print("error en api: {}".format(e))
            self.config(messagebox.showinfo(message="Se ha prodocido un error en la API, intentalo más tarde", title="ERROR EN API"))
            return 

        self.valorAct.config(text=sum(valorAct))

            

    def saldo(self):
       
        saldo =Toplevel()
        saldo.geometry("500x400")
        saldo.title("Saldo Criptos")
        saldo.iconbitmap("imagenes/bolsa.ico")
        saldo.grab_set()

        tabla=ttk.Treeview(saldo,columns=2)
        tabla.grid(row=4,column=0, columnspan=2)
        tabla.heading("#0", text="Cripto", anchor=CENTER)
        tabla.heading("#1", text="Valor", anchor=CENTER)

        try:
            conn = sqlite3.connect(DBFILE)
            c = conn.cursor()

            c.execute( "SELECT CurrencyT , CurrencyQ from MOVEMENTS ;")
            criptoSaldo = c.fetchall()
            dictCripto={}
            for elements in criptoSaldo:
                if elements[0] in dictCripto:
                    dictCripto[elements[0]] += elements[1]
                else:
                    dictCripto[elements[0]] = elements[1]

            if 'EUR' in dictCripto:
                del dictCripto['EUR']
        
            conn.commit()
            conn.close()  
        except Exception as e:
            print( "se ha producido un error en status: {}".format(e))
            self.config(messagebox.showerror(message="error acceso base de datos", title=" ERROR BD"))
  

            
        for k, v in dictCripto.items():
            tabla.insert('',0,text=k, values=v)






        


        





            


 












        

    
