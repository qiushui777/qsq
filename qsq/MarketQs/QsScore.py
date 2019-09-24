import pandas as pd
import numpy as np

from . import QsStat
from ..UtilQs import QsScaleUtil

class QsScore(object):
    """
    策略评价模块, 使用者需要自己设定打分项和比例，否则使用默认值
    """
    def __init__(self):
        self.factor = ["total_return","volatility","sharpe_ratio","information_ratio","alpha","beta","max_drawdown",\
                            "win_rate"]
        self.weight = len(self.factor) * [1/len(self.factor),]
        self.accounts = {} #字典形式，存储所有想要进行比较的QsAccount类


    def cal_score(self):
        """
        计算各个策略结果的得分，最终计算完成后传回的DataFrame如下
            total_return volatility ...
        a1  100            6
        a2  200            5
                    ...
        """
        score_matrix = pd.DataFrame(columns = self.factor)

        for k in self.accounts.keys():
            #增加一行，每个参数设为NaN
            score_matrix.loc[k] = np.NaN
            for f in self.factor:
                score_matrix.loc[k][f] = self.get_factor_value(self.accounts[k], f)
        #按照每列的最大值和最小值进行0-1缩放处理
        score_matrix =  QsScaleUtil.min_max_scaler(score_matrix)
        return score_matrix*self.weight

    def get_factor_value(self, account, factor):
        """
        获取每个因子对应的值
        """
        if factor == "total_return":
            return (account.asset['asset'][-1] - account.asset['asset'][0]) / account.asset['asset'][0]
        if factor == "volatility":
            return QsStat.volatility(account.asset['p_change'])
        if factor == "sharpe_ratio":
            return QsStat.sharpe_ratio(account.asset['p_change'])
        if factor == "information_ratio":
            return QsStat.information_ratio(account.asset['p_change'],account.benchmark.crypto_df['p_change'])
        if factor == "alpha":
            return QsStat.alpha_beta(account.asset['p_change'],account.benchmark.crypto_df['p_change'])[0]
        if factor == "beta":
            return QsStat.alpha_beta(account.asset['p_change'],account.benchmark.crypto_df['p_change'])[1]
        if factor == "max_drawdown":
            return QsStat.max_drawdown(account.asset['p_change'])
        if factor == "win_rate":
            return QsStat.win_rate(account)






