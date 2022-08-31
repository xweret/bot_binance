import binance
import time

API_KEY = ''
API_SECRET = ''

client = binance.Client(api_key=API_KEY, api_secret=API_SECRET)

#%%
precio = float(client.get_klines(symbol = "BTCUSDT", interval = "1m", limit = "1")[0][4])
def actualizar_precio ():
    precio = float(client.get_klines(symbol = "BTCUSDT", interval = "1m", limit = "1")[0][4])
def sell_bitcoin():
    print("selling btc")
    print(precio)
#%%

while True:
    actualizar_precio()
    if precio > 20000:
        print('Paso los 20k')
        actualizar_precio()
        print(precio)
        time.sleep(5)
        pass
    else :
        print('No paso los 20k')
        print(precio)
        sell_bitcoin()
        print('Selling BTC')
        break
        time.sleep(5)


actualizar_precio()
