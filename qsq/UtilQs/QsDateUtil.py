# -*- encoding:utf-8 -*-
"""
    时间日期工具模块
"""

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import datetime
import time
import calendar
from datetime import datetime as dt

"""默认的时间日期格式，项目中金融时间序列等时间相关默认格式"""
K_DEFAULT_DT_FMT = "%Y-%m-%d"

def qs_cmformat_date(datestring):
    """
    输入'Apr 28, 2013' 转换为 2013-04-28
    """
    month_day = datestring.split(',')[0]
    year = datestring.split(',')[1].strip()
    month = str(list(calendar.month_abbr).index(month_day.split(' ')[0]))
    if(len(month) == 1):
        month = '0' + month
    day = month_day.split(' ')[1]
    formated_date = "%s-%s-%s" % (year,month,day)
    return(formated_date)


def fmt_epoch(epoch_time):
    """
    conver the unix time with milliseconds to datetime
    https://stackoverflow.com/questions/21787496/converting-epoch-time-with-milliseconds-to-datetime
    """
    s, ms = divmod(epoch_time, 1000) 
    fmt_time = time.strftime('%Y-%m-%d', time.gmtime(s))
    return fmt_time

def datestr_unixm(datestr):
    """
    Binance accept the unix time with millionseconds
    so we need to convert the str to unix time
    https://stackoverflow.com/questions/19801727/convert-datetime-to-unix-timestamp-and-convert-it-back-in-python
    """
    return(int(time.mktime(str_to_datetime_fast(datestr).timetuple())*1000))

def date_str_to_int(date_str, split='-', fix=True):
    """
    eg. 2016-01-01 -> 20160101
    不使用时间api，直接进行字符串解析，执行效率高
    :param date_str: %Y-%m-%d形式时间str对象
    :param split: 年月日的分割符，默认'-'
    :param fix: 是否修复日期不规范的写法，eg. 2016-1-1 fix 2016-01-01
    :return: int类型时间
    """
    string_date = date_str.replace(split, '')
    return int(string_date)

def week_of_date(date_str, fmt=K_DEFAULT_DT_FMT, fix=True):
    """
    输入'2016-01-01' 转换为星期几，返回int 0-6分别代表周一到周日
    :param date_str: 式时间日期str对象
    :param fmt: 如date_str不是%Y-%m-%d形式，对应的格式str对象
    :param fix: 是否修复日期不规范的写法，eg. 2016-1-1 fix 2016-01-01
    :return: 返回int 0-6分别代表周一到周日
    """

    return dt.strptime(date_str, fmt).weekday()