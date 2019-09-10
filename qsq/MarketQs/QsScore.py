from . import QsStat

class QsScore(object):
    """
    策略评价模块, 使用者需要自己设定打分项和比例，否则使用默认值
    """
    def __init__(self, account):
        self.factor = ["total_return","volatility","sharpe_ratio","information_ratio","alpha","beta","max_drawdown",\
                            "win_rate"]
        self.weight = len(self.factor) * [1/len(self.factor),]
        self.account = account


    def cal_score(self):
        pass



