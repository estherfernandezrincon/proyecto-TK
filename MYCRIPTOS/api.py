import requests

#from MYCRIPTOS import entidades

apiKey="7cbc308d-5a35-45c2-bfe2-c8da53d30f41"



class PeticionError(Exception):
    pass

def peticion(self):
        
    CurrencyFrom = self.CurrencyFrom.get() 
    Qf = float(self.QFrom.get())
    CurrencyTo = self.CurrencyTo.get()
    #url_template = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY=7cbc308d-5a35-45c2-bfe2-c8da53d30f41".format(Qf, CurrencyFrom, CurrencyTo)
    respuesta = requests.get(url_template)

    if respuesta.status_code == 200:      
        datos = respuesta.json()   
        CurrencyPurchase = datos["data"]["quote"][CurrencyTo]["price"]
        self.QTo.set(CurrencyPurchase)
        if datos["data"]["quote"][CurrencyTo]["price"] <= 0 :
            print ("cripto elegida tiene importe inferior a cero")

        elif  datos["data"]["quote"][CurrencyTo]["price"] > 0 :
            respuesta = url_template.format( Qf, CurrencyFrom, CurrencyTo, apiKey)    
    else:
        print("Error de consulta: {}".format(respuesta.status_code))