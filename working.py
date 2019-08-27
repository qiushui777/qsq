from qsq import QsCoinMkScraper

scraper = QsCoinMkScraper()
#scraper.get_all_kline_data()
scraper.refresh_all_kline_data()

"""
from abupy import QsDataMarket,ABuMarketDrawing

qsmarket = QsDataMarket()
bitcoin = qsmarket.get_coin_df(coin='bitcoin')
ethereum = qsmarket.get_coin_df(coin='ethereum')
litecoin = qsmarket.get_coin_df(coin='litecoin')
#ABuMarketDrawing.plot_simple_two_stock({'btc': bitcoin, 'eth': ethereum})
ABuMarketDrawing.plot_multi_df({'bitcoin':bitcoin,'ethereum':ethereum,'litecoin':litecoin})


# scraper test
scraper = QsCoinMkScraper()

#scraper.refresh_kline_data(refresh_cointype='bitcoin')
#scraper.get_all_kline_data()
#scraper.get_kline_data(cointype='tron')
scraper.refresh_all_kline_data()



#binance api test
import requests
import abupy


#print(requests.get(url='https://api.binance.com/api/v1/klines',params={"symbol":"BTCUSDT","interval": "1d", 
    #"startTime":1543104000000, "endTime":1543248000000}).text)
print(requests.get(url='https://api.binance.com/api/v1/klines',params={"symbol":"BTCUSDT","interval": "1d"}).text)



#huobi api test
import websockets
import asyncio
 
async def hello():
    async with websockets.connect('wss://api.huobi.pro/ws') as websocket:
        name = { "sub": "market.ethbtc.kline.1min",  "id": "id1"}
        await websocket.send(name)
        print(f"send server:{name}")
        greeting = await websocket.recv()
        print(f"receive from server:{greeting}")

asyncio.get_event_loop().run_until_complete(hello())
"""