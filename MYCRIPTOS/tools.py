import requests


from configparser import ConfigParser

c= ConfigParser()
c.read('MYCRIPTOS/config.ini')
config = c ['DEFAULT']
APIkey= config['APIkey']

def peticion(CurrencyF, Qf, CurrencyT):
    
    url_template = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}".format(Qf, CurrencyF, CurrencyT,APIkey)
    respuesta = requests.get(url_template)


    if respuesta.status_code == 200:      
        datos = respuesta.json()   
        CurrencyPurchase = round(datos["data"]["quote"][CurrencyT]["price"], 8)
        
        
        return CurrencyPurchase
    else:
        raise Exception("api error : {}".format(respuesta.status_code))







