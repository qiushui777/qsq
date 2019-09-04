import numpy as np
from qsq import QsData, QsCrypto, QsAccount, QsSignal, QsPickSignal, QsDrawUtil

data = QsData()
bitcoin = QsCrypto('bitcoin', data.get_coin_df(coin='bitcoin'))
bitcoin.add_period_max(12)
bitcoin.add_period_min(15)


class buysignal(QsSignal):
    def produce_signal(self,param):
        if self.crypto.crypto_df.loc[param]['12_period_max'] == np.NaN:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}
        if self.crypto.crypto_df.loc[param]['close'] > self.crypto.crypto_df.loc[param]['12_period_max']:
            return {'mode':1, 'symbol':self.crypto.symbol,'percent':1}
        else:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}

class sellsignal(QsSignal):
    def produce_signal(self,param):
        if self.crypto.crypto_df.loc[param]['15_period_min'] == np.NaN:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}
        if self.crypto.crypto_df.loc[param]['close'] < self.crypto.crypto_df.loc[param]['15_period_min']:
            return {'mode':2, 'symbol':self.crypto.symbol,'percent':1}
        else:
            return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}

buy_sig = buysignal(bitcoin)
sell_sig = sellsignal(bitcoin)


myaccount = QsAccount()
QsPickSignal.signal_day_back_test(myaccount,buy_sig,sell_sig)

QsDrawUtil.plot_dfs({'bitcoin':bitcoin.crypto_df.close, 'asset':myaccount.asset.asset})