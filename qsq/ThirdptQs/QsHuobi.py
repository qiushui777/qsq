from ..CoreQs import QsEnv

from huobi import RequestClient, SubscriptionClient
from huobi.model import *
from configparser import ConfigParser

class QsHuobi(object):
    """
    qsq系统提供的火币接口，可通过此接口获取数据和交易等
    要想进行交易，必须在qs/config/config.ini中设置好自己的火币api密钥
    """
    def __init__(self):
        [self.api_key, self.secret_key] = self.get_apikey()
        self.request_client = RequestClient()
        #self.subscription_client = SubscriptionClient()

    def get_apikey(self): 
        cfg = ConfigParser()
        cfg.read(QsEnv.g_project_config)
        return [cfg.get('huobi','huobiapi_key'),cfg.get('huobi','huobisecret_key')]

    def get_24h_trade_statistics(self, pair="btcusdt"):
        """
        param: pair 想要获取的交易对，默认为btcusdt

        获取24小时的市场数据，返回结构体成员包括有
        timestamp, high, low, open, close, volume
        可使用trade_statistics.high这样的方式获取对应数据
        """
        trade_statistics = self.request_client.get_24h_trade_statistics(pair)
        return trade_statistics

    def get_latest_candlestick(self, pair="btcusdt", interval=CandlestickInterval.MIN1, size=10):
        """
        param: pair 想要获取的交易对，默认为btcusdt
        param: interval 时间间隔，默认为MIN1, 可选有MIN1 MIN5 MIN15 MIN30 MIN60 DAY1 MON1 WEEK1 YEAR1 
        param: size 获取的数据条数，默认为10,选择范围为[1,2000]

        获取最近一段时间的K线数据，返回一个list，这个list的每一项的结构体成员包括有
        timestamp, high, low, open, close, volume
        可使用member.high这样的方式获取对应数据
        """
        candlestick_list = self.request_client.get_latest_candlestick(pair, interval, size)
        return candlestick_list