# -*- encoding:utf-8 -*-

import numpy as np

class QsCrypto(object):
    """操作加密货币数据类"""
    def __init__(self, df):
        self.crypto_df = df

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