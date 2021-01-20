from tkinter import *
from tkinter import ttk



root = Tk()
root.geometry("1000x400")
root.title("MY CRIPTO")
root.config( bd= 15, relief="groove")
root.iconbitmap("imagenes/bolsa.ico")



# -------------parte superior PARRILLA y boton + -------------------

frame_five = Frame(root)
parrilla = Frame(frame_five)
parrilla.pack(side= TOP)
frame_five.pack(side=TOP)

labelFecha = Label(text= "Fecha", width=7)
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

frame_one = Frame(root)
FromCurrency = Frame(frame_one)
From = Frame(FromCurrency)

label_FromCurrency = Label(FromCurrency, text= 'From:', width=5)
label_FromCurrency.pack(side= LEFT, fill= X,  padx= 10, pady= 10)

FromMoneda= StringVar()
combo= ttk.Combobox(FromCurrency,  values=("EUR"))
combo.pack(side=LEFT)
FromCurrency.pack(side=TOP)
frame_one.pack(side=LEFT, fill= X)
#FromCurrency.config(bg="pink")



QCurrency = Frame(frame_one)
Q = Frame(QCurrency)
label_QCurrency = Label(QCurrency, text= 'Q:', width= 5)
label_QCurrency.pack(side=LEFT, fill= X,  padx=10, pady=10)
textQ = Entry (QCurrency, width= 23)
textQ.pack(side=LEFT, fill= X,  padx=10, pady=10)
QCurrency.pack(side=TOP)
frame_one.pack(side= LEFT, padx= 65, fill= X)
#QCurrency.config(bg="blue")


# ---------------parte central entrada  TO, Q , PU -------------------
frame_two = Frame(root)
ToCurrency = Frame(frame_two)
To= Frame(ToCurrency)
label_ToCurrency = Label(ToCurrency, text= 'To:', width= 5)
label_ToCurrency.pack(side= LEFT, fill= BOTH, expand= True)

combo= ttk.Combobox(ToCurrency,  values=("EUR","BTC", "ETH", "XRP", "LTC", "BCH", "BNB", "USDT", "EOS", "BSV", "XLM", "ADA", "TRX"))
combo.pack(side=LEFT)
ToCurrency.pack(side=TOP)
frame_two.pack(side=RIGHT, fill= X)
#ToCurrency.config(bg="yellow")

QCurrency = Frame(frame_two)
Q= Frame(QCurrency)
label_QCurrency = Label(QCurrency, text= 'Q:', width= 5)
label_QCurrency.pack(side=LEFT, fill= BOTH, expand= True)

textQ = Entry (QCurrency, width= 23)
textQ.pack(side=LEFT, fill= BOTH, expand= FALSE, padx= 10, pady= 10)
QCurrency.pack(side=TOP)
frame_two.pack(side= LEFT, fill= X)
#QCurrency.config(bg="green")

PU = Frame(frame_two)
label_PU = Label(PU, text= 'P.U.:', width= 5)
label_PU.pack(side=LEFT, fill= BOTH, expand= FALSE)
textPU = Entry (PU, width = 23)
textPU.pack(side=LEFT, fill= BOTH, expand= TRUE, padx= 10, pady= 10)
PU.pack(side=TOP)
frame_two.pack(side= LEFT, fill= X)
#PU.config(bg="black")

#---------------parte central botones ACEPTAR, CANCELAR, OK-----------

frame_three = Frame(root)
Teclas = Frame(frame_three)
Teclas.pack(side= BOTTOM)
frame_three.pack(side=LEFT, fill= X)
frame_three.pack_propagate(FALSE)
#frame_three.config(bg="black")

def Botones():
    FromMoneda.set("moneda seleccionada")

buttonA = Button( text='Aceptar', command= Botones)
buttonA.place(x= 603 , y= 140)
buttonC = Button( text='Cancelar',command= Botones)
buttonC.place(x= 600 , y=170)
buttonOk = Button( text='ok',command= Botones)
buttonOk.place(x= 615 , y=205)

labelNTransaccion = Label(text= "---------Nueva Transaccion------------------------------------------------")
labelNTransaccion.place(x= 60, y= 90)





#----------parte inferior € INVERTIDOS, VALOR ACTUAL, CALCULAR-------------------

frame_four = Frame(root)
Resumen= Frame(frame_four)
Resumen.pack(side=BOTTOM, padx= 10, pady= 5, ipadx= 15)
#Resumen.config(bg="blue")



label_Resumen= Label(Resumen, text="€ invertidos:", width= 10, relief= GROOVE)
label_Resumen.pack(side= LEFT, fill= BOTH, expand= True, padx= 5, pady= 5)
text = Entry(Resumen, width= 15)
text.pack(side=LEFT, padx=5, pady=5)
frame_four.pack(side=BOTTOM)


label_Resumen= Label(Resumen, text=" Valor actual", width= 10)
label_Resumen.pack(side=LEFT,fill= BOTH, expand= True, padx= 5, pady= 5)
text= Entry(Resumen, width= 15)
text.pack(side= LEFT, padx= 5, pady=5)
frame_four.pack(side=BOTTOM)


def CalcularInversion():
    pass

botonCalcular = Button(Resumen,text="Calcular", command=CalcularInversion, relief= GROOVE)
botonCalcular.pack(side= LEFT)
#botonCalcular.place(x= 920, y= 320)
frame_four.pack(side= BOTTOM)

separar=ttk.Separator(frame_four, orient=HORIZONTAL)
separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)



root.mainloop()