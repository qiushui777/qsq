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
        使用输入的参数生成买卖信号
        """
        return [1, self.crypto.symbol]