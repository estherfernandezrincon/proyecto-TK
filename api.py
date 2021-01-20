import requests




direccion = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1000&symbol=EUR&convert=BTC&CMC_PRO_API_KEY=7cbc308d-5a35-45c2-bfe2-c8da53d30f41"

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos= respuesta.json()
    print(datos)
else:
    print("se ha producido un error", respuesta.status_code)