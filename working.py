""" 更新数据
from qsq import QsCoinMkScraper

scrapper = QsCoinMkScraper()
scrapper.refresh_all_kline_data()
"""

from qsq import QsHuobi
from huobi.model import *

qshuobi = QsHuobi()

order_id = qshuobi.order(symbol="btmbtc", account_type=AccountType.SPOT, order_type=OrderType.SELL_MARKET, amount=10)
print("after order, we have order id: " + str(order_id))

order = qshuobi.get_order(symbol="btmbtc", order_id=order_id)
print(order.created_timestamp)