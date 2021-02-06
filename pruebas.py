from tkinter import *
from tkinter import ttk
import datetime

root = Tk()
root.geometry("732x150")
fontH = ("Courier", 14, "bold")
fontL = ("Courier", 14)
movimientos = [('2021-02-04', '19:45:58.056922', 'EUR', 1000.0, 'BTC', 0.03224635), ('2021-02-04', '20:01:58.015093', 'ETH', 1.0, 'LTC', 11.2204221), ('2021-02-04', '20:57:12.292320', 
'LTC', 5.0, 'ETH', 0.44679419), ('2021-02-04', '21:13:25.349782', 'LTC', 5.0, 'EUR', 618.23064996), ('2021-02-04', '21:13:58.606389', 'EUR', 500.0, 'EOS', 195.33198755), 
('2021-02-04', '21:14:52.525784', 'LTC', 5.0, 'EOS', 241.50985277), ('2021-02-04', '21:16:21.921318', 'EUR', 1000.0, 'BNB', 21.37117814), ('2021-02-04', '21:16:51.006286', 'EOS', 50.0, 'EUR', 128.10337998),
('2021-02-04', '21:17:24.280892', 'EUR', 2000.0, 'ETH', 1.43883771), ('2021-02-04', '21:17:49.580235', 'BNB', 10.0, 'EUR', 467.74265374), ('2021-02-04', '21:18:04.583725', 'EUR', 300.0, 'EOS', 117.0920999), 
('2021-02-05', '11:34:15.122407', 'EUR', 1000.0, 'BTC', 0.03196971), ('2021-02-05', '11:43:29.201145', 'EUR', 4000.0, 'LTC', 31.15425594), ('2021-02-05', '17:50:12.100198', 'EOS', 100.0, 'BSV', 1.73524349), 
('2021-02-05', '17:50:13.993053', 'EOS', 100.0, 'BSV', 1.73524349), ('2021-02-05', '18:23:23.194300', 'EUR', 100.0, 'BTC', 0.0031874), ('2021-02-05', '18:35:48.883556', 'EUR', 100.0, 'BTC', 0.00318474), 
('2021-02-06', '12:29:07.942170', 'EOS', 100.0, 'ADA', 596.45227396)] 

cabecera1 = "   Fecha     Hora   From      Cantidad        To       Cantidad        Precio unitario  "
cabecera2 = "---------- -------- ---- ------------------- --- ------------------- -------------------"
fLinea = "{} {}  {} {:19.9f} {} {:19.9f} {:19.9f}"

# Crear cabeceras arriba a la izquierda
lblH1 = Label(root, text=cabecera1, font = fontH, width=88)
lblH1.pack(side=TOP, anchor=W)

lblH2 = Label(root, text=cabecera2, font = fontH, width=88)
lblH2.pack(side=TOP, anchor=W)

#Crear listbox scrollable abajo a la izquierda
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, font=fontL, bd=0 )
for line in movimientos:
    mylist.insert(END, fLinea.format(line['fecha'], line['hora'], 
                                     line['from'], line['qfrom'],
                                     line['to'], line['qto'], line['pu'])
mylist.pack( side = LEFT, fill = BOTH , expand = True)
scrollbar.config( command = mylist.yview )


root.mainloop()
