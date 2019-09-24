import numpy as np
import pandas as pd
from datetime import timedelta
from qsq import QsData, QsCrypto, QsAccount, QsSignal, QsPickSignal, QsDrawUtil, QsStat, QsScaleUtil, QsScore



data = QsData()
bitcoin = QsCrypto('bitcoin', data.get_coin_df(coin='bitcoin')[-60:])


bitcoin.add_window_mean(3)
bitcoin.add_window_mean(5)
bitcoin.add_window_mean(10)

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

class sellsignal2(QsSignal):
    def produce_signal(self,param):
        if self.crypto.crypto_df.loc[param]['10_window_mean'] == np.NaN:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}
        if self.crypto.crypto_df.loc[param]['3_window_mean'] < self.crypto.crypto_df.loc[param]['10_window_mean'] \
            and self.crypto.crypto_df.loc[param - timedelta(days=1)]['3_window_mean'] > \
                        self.crypto.crypto_df.loc[param - timedelta(days=1)]['10_window_mean']:
            return {'mode':2, 'symbol':self.crypto.symbol,'percent':1}
        else:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}

buy_sig = buysignal(bitcoin)
sell_sig = sellsignal(bitcoin)
sell_sig2 = sellsignal2(bitcoin)


myaccount = QsAccount()
myaccount2 = QsAccount()
myaccount.benchmark = bitcoin
myaccount2.benchmark = bitcoin
QsPickSignal.signal_backtest_percent(myaccount,buy_sig,sell_sig)
QsPickSignal.signal_backtest_percent(myaccount2,buy_sig,sell_sig2)

myaccount.cal_returns()
myaccount2.cal_returns()

score = QsScore()
score.accounts = {"a1":myaccount,"a2":myaccount2}
print(score.cal_score())


#QsDrawUtil.plot_dfs({'bitcoin':bitcoin.crypto_df.close, 'asset':myaccount.asset.asset})
