from ..CoreQs import QsEnv

from huobi import RequestClient, SubscriptionClient
from huobi.base.printobject import PrintMix
from huobi.model import *
from configparser import ConfigParser

class QsHuobi(object):
    """
    qsq系统提供的火币接口，可通过此接口获取数据和交易等
    要想进行交易，必须在qs/config/config.ini中设置好自己的火币api密钥
    """
    def __init__(self):
        [self.api_key, self.secret_key] = self.get_apikey()
        self.request_client = RequestClient(api_key=self.api_key, secret_key=self.secret_key)
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

    def get_exchange_currencies(self):
        """
        获取火币所有交易币种
        """
        return self.request_client.get_exchange_currencies()

    def get_exchange_info(self):
        """
        获取交易所信息，返回交易对和支持币种，使用案例
        for symbol in exchange_info.symbol_list:
            print(symbol.symbol)
    
        for currency in exchange_info.currencies:
            print(currency)
        """
        return self.request_client.get_exchange_info()

    def get_fee_rate(self, symbol="btcusdt"):
        """
        获取交易手续费，返回一个FeeRate对象，成员包括
        symbol 对应币种 maker_fee 卖方手续费 taker_fee 买方手续费
        实际使用中，symbol也为一个费率
        """
        result = self.request_client.get_fee_rate(symbols=symbol)
        return result[0]

    def get_historical_orders(self, symbol="ethusdt", order_state=OrderState.CANCELED, order_type=None, start_date=None, end_date=None, start_id=None, size=None):
        """
        param: symbol 符号(必须)
        param: order_state 订单状态(必须)，可选参数有SUBMITTED PARTIAL_FILLED CANCELLING PARTIAL_CANCELED FILLED CANCELED INVALID
        param: order_type 订单类型(可选)，可选参数有SELL_LIMIT BUY_LIMIT BUY_MARKET SELL_MARKET BUY_IOC SELL_IOC BUY_LIMIT_MAKER SELL_LIMIT_MAKER BUY_STOP_LIMIT SELL_STOP_LIMIT INVALID 
        param: start_date 开始日期(可选) 格式为 yyyy-mm-dd
        param: end_date 结束日期(可选) 格式为 yyyy-mm-dd
        param: start_id(可选) 订单起始id，暂时忽略
        param: size(可选) 大小，暂时忽略
        
        获取历史订单
        """
        orders = self.request_client.get_historical_orders(symbol=symbol, order_state=order_state, order_type=order_type, start_date=start_date, end_date=end_date, start_id=start_id, size=size)
        return orders

    def get_historical_trade(self, symbol="btcusdt", size=5):
        """
        param: symbol 符号(必须)
        param: size 交易列表的大小(必须)
        获取历史交易数据，返回trade_list对象列表，每个对象有如下几个成员
        timestamp trade_id price amount direction
        """
        trade_list = self.request_client.get_historical_trade(symbol,size)
        return trade_list

    def get_market_trade(self,symbol="btcusdt"):
        trades = self.request_client.get_market_trade(symbol=symbol)
        if(len(trades)):
            for trade in trades:
                print(trade)
                trade.print_object()