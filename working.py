""" 更新数据
from qsq import QsCoinMkScraper

scrapper = QsCoinMkScraper()
scrapper.refresh_all_kline_data()
"""
import numpy as np

from qsq import QsCrypto, QsHmm

bitcoin = QsCrypto('bitcoin')
bitcoin.add_nday_logreturn(5)

print(bitcoin.crypto_df)

"""
a = np.array((1,2,3))
b = np.array((2,3,4))
temp_state = np.column_stack((a,b))


hmm = QsHmm()
hmm.components = 2
hmm.fit(temp_state)
print(hmm.hidden_state)
"""