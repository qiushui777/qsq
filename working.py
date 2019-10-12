""" 更新数据
from qsq import QsCoinMkScraper

scrapper = QsCoinMkScraper()
scrapper.refresh_all_kline_data()
"""

from qsq import QsHuobi

qshuobi = QsHuobi()
data = qshuobi.get_market_trade()