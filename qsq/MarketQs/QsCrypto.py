# -*- encoding:utf-8 -*-

import numpy as np
import pandas as pd

from .QsData import QsData

class QsCrypto(object):
    """操作加密货币数据类"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.crypto_df = QsData().get_coin_df(coin=symbol)

    def add_period_max(self, period):
        """
        增加一列，获取n天内close列的最大值
        param: period int值，时间区段的长度
        目前这个n天不包括今日
        """
        self.crypto_df[str(period)+'_period_max'] = np.NaN
        for i in range(period, len(self.crypto_df)):
            self.crypto_df.ix[i,str(period)+'_period_max'] = self.crypto_df[i-period:i]['close'].max()
        
    def add_period_min(self, period):
        """
        增加一列，获取n天内close列的最小值
        param: period int值，时间区段的长度
        目前这个n天不包括今日
        """
        self.crypto_df[str(period)+'_period_min'] = np.NaN
        for i in range(period, len(self.crypto_df)):
            self.crypto_df.ix[i,str(period)+'_period_min'] = self.crypto_df[i-period:i]['close'].min()

    def add_window_mean(self, window):
        """
        增加一列，获取n天内的均值
        param: window int值，时间区段的长度
        """
        self.crypto_df[str(window)+'_window_mean'] = np.round(self.crypto_df.close.rolling(window=window).mean(),2)

    def add_nday_logreturn(self, n):
        """
        增加n天对数收益差
        """

        for i in range(n, len(self.crypto_df)):
            self.crypto_df.ix[i,str(n)+'day_logreturn'] = np.log(self.crypto_df.ix[i,'close']) - \
                                                                    np.log(self.crypto_df.ix[i-n,'close'])