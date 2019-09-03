# -*- encoding:utf-8 -*-

class QsSignal(object):
    """
    信号基类，用于给出买卖操作
    """
    def __init__(self,crypto):
        # 此处crypto为跟踪的币种价格信息
        self.crypto = crypto

    def produce_signal(self, param):
        """
        使用输入的参数生成买卖信号，返回一个字典，包含 
        mode: 买卖方向
        symbol: 买卖对象
        percent: 买卖比例 
        """
        return {'mode':0, 'symbol':self.crypto.symbol,'percent':1}