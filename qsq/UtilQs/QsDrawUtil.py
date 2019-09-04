# -*- encoding:utf-8 -*-
"""
    绘图工具模块
"""


from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import matplotlib.pyplot as plt

from . import QsScaleUtil

def plot_multi_df_close(multi_kl_dict):
    """
    将多个金融时间序列收盘价格缩放到一个价格水平后，可视化价格变动
    abu原先的多股票代码存在bug，此处稍作更改
    :param multi_kl_dict: 字典形式，key将做为lable进行可视化使用，元素为金融时间序列
    """
    if not isinstance(multi_kl_dict, dict):
        print("[qiushui log] multi_kl_dict must be a dict")
        return

    label_arr = [s_name for s_name in multi_kl_dict.keys()]
    df_lists = []
    for key in label_arr:
        df_lists.append(multi_kl_dict[key].close)
    scale_factors = QsScaleUtil.scale_dfs(df_lists)
    for i in range(len(df_lists)):
        df_lists[i] = df_lists[i] * scale_factors[i]
        plt.plot(df_lists[i], label=label_arr[i])
    plt.legend(loc='upper left')
    plt.show()
    return

def plot_dfs(dfs_dict):
    """
    直接绘制多个单列dataframe，传入参数为字典，形式如: {'btc':bitcoin,'eth':ethereum}
    """
    label_arr = [s_name for s_name in dfs_dict.keys()]
    df_lists = []
    for key in label_arr:
        df_lists.append(dfs_dict[key])
    scale_factors = QsScaleUtil.scale_dfs(df_lists)
    for i in range(len(df_lists)):
        df_lists[i] = df_lists[i] * scale_factors[i]
        plt.plot(df_lists[i], label=label_arr[i])
    plt.legend(loc='upper left')
    plt.show()
    return