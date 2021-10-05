import requests as req

url = "https://rest.coinapi.io/v1/exchangerate/SLP/EUR"
apikey = "DF48B51C-50D6-4F3E-9479-0C72F83F4695"

cabecera = {"X-CoinAPI-Key": apikey}

seguir = 's'
while seguir == 's':
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")
    respuesta = req.get(url.format (de, a), headers=cabecera)

    if respuesta.status_code ==200:
        print (respuesta.json()['rate'])
    else:
        print (respuesta.status_code)
        print (respuesta.json())

    seguir = input("¿Quieres más? (S/N): ").lower()

