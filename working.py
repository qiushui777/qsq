import numpy as np
import pandas as pd
from datetime import timedelta
from qsq import QsData, QsCrypto, QsAccount, QsSignal, QsPickSignal, QsDrawUtil, QsStat, QsScaleUtil, QsScore

data = QsData()
bitcoin = QsCrypto('bitcoin', data.get_coin_df(coin='bitcoin')[-90:])


bitcoin.add_window_mean(3)
bitcoin.add_window_mean(5)

class buysignal(QsSignal):
    def produce_signal(self,param):
        if self.crypto.crypto_df.loc[param]['5_window_mean'] == np.NaN:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}
        if self.crypto.crypto_df.loc[param]['3_window_mean'] > self.crypto.crypto_df.loc[param]['5_window_mean'] \
            and self.crypto.crypto_df.loc[param - timedelta(days=1)]['3_window_mean'] < \
                        self.crypto.crypto_df.loc[param - timedelta(days=1)]['5_window_mean']:
            return {'mode':1, 'symbol':self.crypto.symbol,'percent':1}
        else:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}

class sellsignal(QsSignal):
    def produce_signal(self,param):
        if self.crypto.crypto_df.loc[param]['5_window_mean'] == np.NaN:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}
        if self.crypto.crypto_df.loc[param]['3_window_mean'] < self.crypto.crypto_df.loc[param]['5_window_mean'] \
            and self.crypto.crypto_df.loc[param - timedelta(days=1)]['3_window_mean'] > \
                        self.crypto.crypto_df.loc[param - timedelta(days=1)]['5_window_mean']:
            return {'mode':2, 'symbol':self.crypto.symbol,'percent':1}
        else:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}

buy_sig = buysignal(bitcoin)
sell_sig = sellsignal(bitcoin)


myaccount = QsAccount()
QsPickSignal.signal_backtest_percent(myaccount,buy_sig,sell_sig)

myaccount.cal_returns()
print(myaccount.asset)

#QsDrawUtil.plot_dfs({'bitcoin':bitcoin.crypto_df.close, 'asset':myaccount.asset.asset})
