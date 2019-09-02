from qsq import QsData, QsCrypto, QsAccount

data = QsData()
bitcoin = QsCrypto(data.get_coin_df(coin='bitcoin'))
bitcoin.add_period_max(3)
bitcoin.add_period_min(3)

myaccount = QsAccount()
myaccount.Order(date="19-1",mode=1,symbol='bitcoin',price=1000,amount=100)
myaccount.Order(date="19-2",mode=2,symbol='bitcoin',price=1200,amount=100)
print(myaccount.order_df, myaccount.security_df, myaccount.balance)






"""
import matplotlib as mpl

from qsq import QsData, QsDrawUtil, QsStat

qsmarket = QsData()
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




from qsq import QsCoinMkScraper

scraper = QsCoinMkScraper()
#scraper.get_all_kline_data()
scraper.refresh_all_kline_data()


"""