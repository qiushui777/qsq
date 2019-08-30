# -*- encoding:utf-8 -*-

import pandas as pd

class QsAccount(object):
    """
    帐户模型，包括买卖操作、回测等
    """
    def __init__(self):
        self.money = 1000000.00 #初始资金
        self.commission = 0.0005 #交易佣金
        self.stop_loss = True #开启止损模式
        self.stop_loss_num = 0 #止损次数
        self.stop_loss_range = 0.05 #止损幅度

        self.order_df = pd.DataFrame(columns = ['date','time','mode','crypto','amount','price']) #交易记录
        self.security_df = pd.DataFrame(columns = ['crypto','amount','position']) #各币种持仓量