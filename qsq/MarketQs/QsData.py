# -*- encoding:utf-8 -*-

import os
import pandas as pd
from ..CoreQs import QsEnv

class QsData(object):
    """获取数字货币价格数据的类"""

    def __init__(self):
        self.cachedir = QsEnv.g_project_cache_dir

    def get_coin_df(self,coin="bitcoin",start=None,end=None):
        """
        根据币种和时间段返回一个对应的DataFrame
        params: start 开始日期 格式为 '2019-8-11'
        params: end 结束日期 格式为 '2019-8-11'
        """
        coinfile = os.path.join(self.cachedir,self.get_filename_from_coin(coin))
        full_df = pd.read_csv(coinfile,index_col=0)
        # 将index 改为 datetime的形式，否则plt的时候横轴密度很大
        # https://stackoverflow.com/questions/40815238/python-pandas-convert-index-to-datetime
        full_df.index = pd.to_datetime(full_df.index)
        if start is None and end is None:
            return full_df
        elif start is None and end is not None:
            return full_df.loc[:end]
        else:
            return full_df.loc[start:]



    def get_filename_from_coin(self,coinname):
        """根据币的名字获取到对应的数据集名称"""
        target_file_name = 'qs' + coinname
        result_file_name = None
        files = os.listdir(self.cachedir)
        for file in files:
            if target_file_name == file.split("_")[0]:
                result_file_name = file
                break
        if result_file_name is None:
            raise Exception("[qiushui Exception] You haven't got the data")
        return result_file_name