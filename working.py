import matplotlib as mpl

from qsq import QsDataMarket, QsDrawUtil, QsStat

qsmarket = QsDataMarket()
bitcoin = qsmarket.get_coin_df(coin='bitcoin')
ethereum = qsmarket.get_coin_df(coin='ethereum')
litecoin = qsmarket.get_coin_df(coin='litecoin')
ripple = qsmarket.get_coin_df(coin='ripple')
bitcoin_cash = qsmarket.get_coin_df(coin='bitcoin-cash')
mpl.rcParams['figure.figsize'] = (15,10)
#QsDrawUtil.plot_multi_df({'bitcoin':bitcoin,'ethereum':ethereum,'litecoin':litecoin,'ripple':ripple,
                                #'bitcoin_cash':bitcoin_cash})

bitcoin_2y = bitcoin[-730:]
ethereum_2y = ethereum[-730:]
litecoin_2y = litecoin[-730:]
ripple_2y = ripple[-730:]
bitcoin_cash_2y = bitcoin_cash[-730:]

data_week_wave = QsStat.date_week_wave(({'bitcoin':bitcoin,'bitcoin_2y':bitcoin_2y,'ethereum':ethereum,'ethereum_2y':ethereum_2y,
                         'litecoin':litecoin,'litecoin_2y':litecoin_2y,'ripple':ripple,'ripple_2y':ripple_2y,
                         'bitcoin_cash':bitcoin_cash,'bitcoin_cash_2y':bitcoin_cash_2y}))

print(data_week_wave)

"""
from qsq import QsCoinMkScraper

scraper = QsCoinMkScraper()
#scraper.get_all_kline_data()
scraper.refresh_all_kline_data()


from abupy import QsDataMarket,ABuMarketDrawing

qsmarket = QsDataMarket()
bitcoin = qsmarket.get_coin_df(coin='bitcoin')
ethereum = qsmarket.get_coin_df(coin='ethereum')
litecoin = qsmarket.get_coin_df(coin='litecoin')
#ABuMarketDrawing.plot_simple_two_stock({'btc': bitcoin, 'eth': ethereum})
ABuMarketDrawing.plot_multi_df({'bitcoin':bitcoin,'ethereum':ethereum,'litecoin':litecoin})

"""