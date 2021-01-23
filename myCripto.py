from tkinter import *
from tkinter import ttk



root = Tk()
root.geometry("700x400")
root.title("MY CRIPTO")
root.config( bd= 15, relief="groove")
root.iconbitmap("imagenes/bolsa.ico")
root.resizable(0,0)



# -------------parte superior PARRILLA y boton + -------------------

frame_five = Frame(root)
frame_five.pack(side=TOP)


labelFecha = Label( text= "Fecha", width=7)
labelFecha.place(x= 60, y=0)

labelHora = Label(text= "Hora", width=7)
labelHora.place(x= 120, y=0)


labelFrom = Label(text= "From", width=7)
labelFrom.place(x= 180, y=0)


labelQ = Label(text= "Q", width=7)
labelQ.place(x= 240, y=0)

labelTo = Label(text= "To", width=7)
labelTo.place(x= 300, y=0)


labelQ = Label(text= "Q", width=7)
labelQ.place(x=360 , y=0)

labelPU = Label(text= "P.U.", width=7)
labelPU.place(x=420 , y=0)

botonMas = Button(text=" +", width= 5,height=3)
botonMas.place(x=500, y= 20)


entryFecha = Entry( width=10)
entryFecha.place(x=60, y=25)

entryHora = Entry( width=10)
entryHora.place(x=120, y=25)

entryFrom = Entry( width=10)
entryFrom.place(x=180, y=25)

entryQ = Entry( width=10)
entryQ.place(x=240, y=25 )

entryTo = Entry( width=10)
entryTo.place(x=300, y=25)

entryQ = Entry( width=10)
entryQ.place(x=360, y=25)

entryPU = Entry( width=10)
entryPU.place(x=420, y=25)

entryFecha = Entry( width=10)
entryFecha.place(x=60, y=50)

entryHora = Entry( width=10)
entryHora.place(x=120, y=50)

entryFrom = Entry( width=10)
entryFrom.place(x=180, y=50)

entryQ = Entry( width=10)
entryQ.place(x=240, y=50 )

entryTo = Entry( width=10)
entryTo.place(x=300, y=50)

entryQ = Entry( width=10)
entryQ.place(x=360, y=50 )

entryPU = Entry( width=10)
entryPU.place(x=420, y=50)




# ---------------parte central entrada FROM y Q--------------
fCenter= Frame(root)
frame_one = Frame(fCenter)
frame_one.pack(side=LEFT)

FromCurrency = Frame(frame_one)
From = Frame(FromCurrency)

fCenter.pack(side=TOP)

label_FromCurrency = Label(FromCurrency, text= 'From:', width=5)
label_FromCurrency.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

combo= ttk.Combobox(FromCurrency,  values=("EUR"))
combo.pack(side=LEFT)
FromCurrency.pack(side=TOP)





QCurrency = Frame(frame_one)
Q = Frame(QCurrency)
label_QCurrency = Label(QCurrency, text= 'Q:', width= 5)
label_QCurrency.pack(side=LEFT, fill= X,  padx=10, pady=10)
textQ = Entry (QCurrency, width= 23)
textQ.pack(side=LEFT, fill= X,  padx=10, pady=10)
QCurrency.pack(side=TOP)




# ---------------parte central entrada  TO, Q , PU -------------------
fCenter= Frame( root)
frame_two = Frame(fCenter)
frame_two.pack(side=LEFT)


ToCurrency = Frame(frame_two)
To= Frame(ToCurrency)
label_ToCurrency = Label(ToCurrency, text= 'To:', width= 5)
label_ToCurrency.pack(side= LEFT, fill= BOTH, expand= True)
fCenter.pack(side=TOP)

combo= ttk.Combobox(ToCurrency,  values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"))
combo.pack(side=LEFT)
ToCurrency.pack(side=TOP)


QCurrency = Frame(frame_two)
Q= Frame(QCurrency)
label_QCurrency = Label(QCurrency, text= 'Q:', width= 5)
label_QCurrency.pack(side=LEFT, fill= BOTH, expand= True)


textQ = Entry (QCurrency, width= 23)
textQ.pack(side=LEFT, fill= BOTH, expand= FALSE, padx= 10, pady= 10)
QCurrency.pack(side=TOP)



PU = Frame(frame_two)
label_PU = Label(PU, text= 'P.U.:', width= 5)
label_PU.pack(side=LEFT, fill= BOTH, expand= FALSE)
textPU = Entry (PU, width = 23)
textPU.pack(side=LEFT, fill= BOTH, expand= TRUE, padx= 10, pady= 10)
PU.pack(side=TOP)



#---------------parte central botones ACEPTAR, CANCELAR, OK-----------
fCenter = Frame(root)
frame_three = Frame(fCenter)
Teclas = Frame(frame_three)
Teclas.pack(side= BOTTOM)

#fCenter.pack(side=TOP)



buttonA = Button( text='Aceptar')
buttonA.place(x= 603 , y= 140)
buttonC = Button( text='Cancelar')
buttonC.place(x= 600 , y=170)
buttonOk = Button( text='Consulta Api')
buttonOk.place(x= 590 , y=205)



labelNTransaccion = Label(text= "---------Nueva Transaccion------------------------------------------------")
labelNTransaccion.place(x= 60, y= 90)





#----------parte inferior € INVERTIDOS, VALOR ACTUAL, CALCULAR-------------------

frame_four = Frame(root)
frame_four.pack(side=TOP)
Resumen= Frame(frame_four)
Resumen.pack(side=BOTTOM, padx= 10, pady= 5, ipadx= 15)




label_Resumen= Label(Resumen, text="€ invertidos:", width= 10)
label_Resumen.pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)
text = Entry(Resumen, width= 15)
text.pack(side=LEFT, padx=5, pady=5)



label_Resumen= Label(Resumen, text=" Valor actual", width= 10 )
label_Resumen.pack(side=LEFT,fill= BOTH, expand= True, padx= 5, pady= 5)
text= Entry(Resumen, width= 15)
text.pack(side= LEFT, padx= 5, pady=5)




botonCalcular = Button(Resumen,text="Calcular", relief= GROOVE)
botonCalcular.pack(side= LEFT)



separar=ttk.Separator(frame_four, orient=HORIZONTAL)
separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

frame_four.pack(side=BOTTOM)

root.mainloop()