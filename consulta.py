import requests as req

url = "https://rest.coinapi.io/v1/exchangerate/AXS/EUR"
apikey = "DF48B51C-50D6-4F3E-9479-0C72F83F4695"

cabecera = {"X-CoinAPI-Key": apikey}
respuesta = req.get(url, headers=cabecera)

print (respuesta.status_code)


midiccionario = respuesta.json()
print(midiccionario['rate'])

#print (respuesta.text)

print (respuesta.json()['rate'])