import requests


apiKey="7cbc308d-5a35-45c2-bfe2-c8da53d30f41"

url_template = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}"



class PeticionError(Exception):
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos= respuesta.json()
        if datos["data"]["quote"][cripto]["price"] <= 0 :
            raise PeticionError("cripto elegida tiene importe inferior a cero")
        else:
            return (datos)
    else:
        raise PeticionError("Error de consulta: {}".format(respuesta.status_code))


respuesta = requests.get(url_template)
datos= respuesta.json()

cantidad = input("qué cantidad quieres invertir: ")
invertir = input("qué moneda vas a invertir: ")
cripto= input("qué cripto quieres comprar : ")
respuesta = peticion (url_template.format(cantidad, invertir, cripto, apiKey ))

cripto_inversion = respuesta["data"]["quote"][cripto]["price"]
print("Has invertido {}, {}, en comprar {}, y el importe es de tu compra es de {}".format(cantidad, invertir, cripto, cripto_inversion))

