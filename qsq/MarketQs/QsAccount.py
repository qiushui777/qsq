# -*- encoding:utf-8 -*-

import pandas as pd

class QsAccount(object):
    """
    帐户模型，包括买卖操作、回测等
    """
    def __init__(self):
        self.balance = 1000000.00 #初始资金
        self.commission = 0.0005 #交易佣金
        self.stop_loss = True #开启止损模式
        self.stop_loss_num = 0 #止损次数
        self.stop_loss_range = 0.05 #止损幅度

        self.order_df = pd.DataFrame(columns = ['date','time','mode','symbol','amount','price','commission_fee']) #交易记录
        self.security_df = pd.DataFrame(columns = ['symbol','amount']) #各币种持仓量

    def Order(self,date=None,time=None,mode=None,symbol=None,amount=None,price=None):
        """
        下单函数
        param: date str 日期
        param: time str 下单时间
        param: mode int 1 为买入 2 为卖出
        param: symbol str 购买目标代号
        param: amount float 购买数量
        param: price float 购买单价
        """
        # 先添加下单流水
        ln = len(self.order_df)
        df_new = pd.DataFrame({'date':date, 'time':time, 'mode':mode, 'symbol':symbol, 'amount':amount, 
                                'price':price, 'commission_fee':amount*price*self.commission}, index = [ln])
        self.order_df = self.order_df.append(df_new, ignore_index=True)

        #买入
        if mode == 1:
            ln = len(self.security_df)
            cost = amount*price*(1+self.commission)
            self.balance -= cost
            # 修改持仓量
            if len(self.security_df[self.security_df.symbol==symbol]) == 0: # 没有持仓
                df_new = pd.DataFrame({'symbol':symbol, 'amount':amount}, index=[ln])
                self.security_df = self.security_df.append(df_new, ignore_index=True)
            else: # 持有该币种
                self.security_df.index = self.security_df['symbol']
                self.security_df.loc[symbol,'amount'] = self.security_df.loc[symbol,'amount'] + amount
                self.security_df=self.security_df.reset_index(level=None, drop=True ,col_level=0, col_fill='')  
        
        ln = len(self.security_df[self.security_df.symbol==symbol])
        # 卖出
        if mode == 2 and ln > 0 : 
            self.security_df.index = self.security_df['symbol']
            # 不能卖超过持有量的数目
            if self.security_df.loc[symbol,'amount'] < amount:
                amount = self.security_df.loc[symbol,'amount']
            income = amount*price*(1-self.commission)
            self.balance += income
            self.security_df.loc[symbol, 'amount'] -= amount
            if self.security_df.loc[symbol, 'amount'] == 0:
                self.security_df = self.security_df.drop(symbol, axis=0)
            self.security_df = self.security_df.reset_index(level=None, drop=True, col_level=0, col_fill='')            


        if mode == 2 and ln == 0:
            raise Exception("[qiushui log]: Selling a non-exist Coin")