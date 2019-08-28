# -*- encoding:utf-8 -*-
"""
    标准规范化数据工具模块
"""

def scale_dfs(df_list, type_look='look_max', mean_how=False):
    """
    仿照scaler_matrix对多个DataFrame进行缩放
    返回每个DataFrame需要缩放的值的list
    """
    if type_look == 'look_max':
        group_max = []
        for df in df_list:
            group_max.append(df.max())
        max_v = max(group_max)
        scale_factor = [ max_v / single_max for single_max in group_max]
    elif type_look == 'look_min':
        group_min = []
        for df in df_list:
            group_min.append(df.min())
        min_v = min(group_min)
        scale_factor = [ min_v / single_min for single_min in group_min]
    return(scale_factor)