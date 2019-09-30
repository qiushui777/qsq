from hmmlearn.hmm import GaussianHMM

class QsHmm(object):
    """
    隐马尔可夫策略
    """
    def __init__(self):
        self.components = 6
        self.model = None
        self.iter = 1000
        self.covariance_type = "diag" #convariance_type 包括有"full","spherical","diag","tied"
        self.hidden_state = None

    def fit(self, fit_data):
        """
        训练隐马尔可夫模型的接口
        """
        self.model = GaussianHMM(n_components=self.components, covariance_type=self.covariance_type, n_iter = self.iter)\
                        .fit(fit_data)
        self.hidden_state = self.model.predict(fit_data)