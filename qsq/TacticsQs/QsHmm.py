from hmmlearn.hmm import GaussianHMM
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class QsHmm(object):
    """
    隐马尔可夫策略
    """
    def __init__(self,crypto_df):
        self.components = 6
        self.model = None
        self.iter = 1000
        self.covariance_type = "diag" #convariance_type 包括有"full","spherical","diag","tied"
        self.hidden_states = None
        self.cryptodata = crypto_df #行情数据

    def fit(self, fit_data):
        """
        训练隐马尔可夫模型的接口
        """
        self.model = GaussianHMM(n_components=self.components, covariance_type=self.covariance_type, n_iter = self.iter)\
                        .fit(fit_data)
        self.hidden_states = self.model.predict(fit_data)

    def plot_hidden_states(self,cut):
        """
        将隐藏状态和市场状态绘制在一起以显示每个隐藏状态的预测效果
        此处的cut指的是训练时截取数据的偏移，如5day_logreturn，cut为5
        """
        plt.figure(figsize=(15, 8))  
        date_index = self.cryptodata[cut:].index
        close_price = self.cryptodata['close'][5:]
        for i in range(self.components):
            idx = (self.hidden_states == i)
            plt.plot_date(date_index[idx],close_price[idx],'.',label='%dth hidden state'%i,lw=1)
            plt.legend()
            plt.grid(1)
        plt.show()

    def plot_states_effect(self,cut):
        """
        在每个隐藏状态为True的第二天买入，观察资产增值情况
        此处的cut指的是训练时截取数据的偏移，如5day_logreturn，cut为5
        """
        date_index = self.cryptodata[cut:].index
        res = pd.DataFrame({'tradeDate':date_index}).set_index('tradeDate')
        plt.figure(figsize=(15, 8))
        for i in range(self.components):
            idx = (self.hidden_states == i)
            idx = np.append(0,idx[:-1]) #将true false转为1 0
            df = self.get_oneday_logreturn()[cut:]
            res['sig_ret%s'%i] = df.multiply(idx,axis=0)
            plt.plot(np.exp(res['sig_ret%s'%i].cumsum()),label='%dth hidden state'%i)
            plt.legend()
            plt.grid(1)
        plt.show()

    def get_oneday_logreturn(self):
        """
        获取数据的1day_logreturn用于观测隐藏状态的效果
        """
        if ('1day_logreturn') in self.cryptodata:
            return self.cryptodata['1day_logreturn']
        else:
            for i in range(1, len(self.cryptodata)):
                self.cryptodata.ix[i,'1day_logreturn'] = np.log(self.cryptodata.ix[i,'close']) - \
                                                                    np.log(self.cryptodata.ix[i-1,'close'])
            return self.cryptodata['1day_logreturn']

