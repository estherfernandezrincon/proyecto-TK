import requests
from MYCRIPTOS.entidades import *

APIkey="7cbc308d-5a35-45c2-bfe2-c8da53d30f41"





def peticion(CurrencyF, Qf, CurrencyT):
    

    
    url_template = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}".format(Qf, CurrencyF, CurrencyT,APIkey)
    respuesta = requests.get(url_template)


    if respuesta.status_code == 200:      
        datos = respuesta.json()   
        CurrencyPurchase = round(datos["data"]["quote"][CurrencyT]["price"], 8)
        
        return CurrencyPurchase

  

    

