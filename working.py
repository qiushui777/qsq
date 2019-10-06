""" 更新数据
from qsq import QsCoinMkScraper

scrapper = QsCoinMkScraper()
scrapper.refresh_all_kline_data()
"""
import numpy as np

from locale import *
from qsq import QsCrypto, QsHmm

setlocale(LC_NUMERIC, 'English_US')

bitcoin = QsCrypto('bitcoin')
bitcoin.crypto_df = bitcoin.crypto_df[-720:]

bitcoin.add_nday_logreturn(1)
bitcoin.add_nday_logreturn(5)
bitcoin.add_high_low_log()

high_low_log = bitcoin.crypto_df['high_low_log'].values[5:]
one_day_logreturn = bitcoin.crypto_df['1day_logreturn'].values[5:]
five_day_logreturn = bitcoin.crypto_df['5day_logreturn'].values[5:]
cap = bitcoin.crypto_df['MarketCap'].values[5:]
cap = [atof(num) for num in cap]


train_data = np.column_stack([high_low_log, one_day_logreturn, five_day_logreturn, cap])

hmm = QsHmm(bitcoin.crypto_df)
hmm.fit(train_data)
#hmm.plot_hidden_states(5)
hmm.plot_states_effect(5)


"""
a = np.array((1,2,3))
b = np.array((2,3,4))
temp_state = np.column_stack((a,b))


hmm = QsHmm()
hmm.components = 2
hmm.fit(temp_state)
print(hmm.hidden_state)
"""