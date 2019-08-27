#coding=utf-8

"""
    爬取CoinMarket网站加密货币价格的爬虫
"""

import datetime
import os
import time
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from ..UtilQs import QsDateUtil
from ..CoreQs import QsEnv




class QsCoinMkScraper(object):
    def __init__(self):
        self.targetcoin = "bitcoin"
        self.start = "20130428"
        self.end = self.getdate()
        self.url = "https://coinmarketcap.com/currencies/%s/historical-data/?start=%s&end=%s"
        self.support_list = ['bitcoin', 'ethereum', 'ripple', 'bitcoin-cash','litecoin',
                            'binance-coin', 'tether', 'eos', 'bitcoin-sv', 'monero', 'stellar', 
                            'unus-sed-leo', 'cardano', 'tron', 'dash', 'chainlink', 'tezos',
                            'ethereum-classic', 'neo', 'iota']

    def getdate(self):
        """获得当日日期"""
        today = datetime.date.today()
        return today.strftime('%Y%m%d')

    def get_kline_data(self, cointype="bitcoin", startdate=None, enddate=None, save = True):
        """
        日K线接口，CoinMartket暂时无法获取更短间隔的数据
        :param startdate: 开始日期，格式为20130501
        :param enddate: 结束日期，格式为20130502    
        """
        print("[qiushui log] Getting the data for " + cointype)
        if cointype not in self.support_list:
            raise Exception("Not support: " + cointype)
        self.targetcoin = cointype
        if startdate is not None:
            self.start = startdate
        if enddate is not None:
            self.end = enddate
        url = self.url % (self.targetcoin, self.start, self.end)
        datadf = self.parse_page(url)
        if(save):
            self.save_cache(datadf)
        return datadf

    def refresh_kline_data(self, refresh_cointype="bitcoin"):
        """
        更新cache中的数据集
        由于使用get_kline_data更新每次请求处理全部数据，在更新较多的数据集的情况下较为费时，所以单独编写更新函数
        """
        # 获取要更新的对应数据文件
        file_list = os.listdir(QsEnv.g_project_cache_dir)
        found = False 
        target_file = ""
        for filename in file_list:
            if refresh_cointype in filename:
                target_file = os.path.join(QsEnv.g_project_cache_dir,filename)
                found = True
                break
        if not found:
            print("[qiushui log] You haven't downloaded the file... Download now :)")
            self.get_kline_data(cointype=refresh_cointype)
            return
        old_df = pd.read_csv(target_file,index_col=0)
        old_df = old_df.applymap(str)
        # 判断数据是否最新
        lastest = old_df.iloc[-1]['date']
        if(int(lastest) < int(self.getdate())-1):
            print("[qiushui log] Refreshing the file: " + filename)
            insert_df = self.get_kline_data(cointype=refresh_cointype,startdate=str(int(lastest)+1), save=False)
            new_pd = pd.concat([old_df, insert_df])
            self.save_cache(new_pd)
            os.remove(target_file)
        else:
            print("[qiushui log] Already up to date for " + refresh_cointype)

    def get_all_kline_data(self):
        """获取所有在support list 中的代币的数据"""
        for coin in self.support_list:
            self.get_kline_data(cointype=coin)
            time.sleep(1)


    def refresh_all_kline_data(self):
        """更新所有在support list中的代币的数据"""
        for coin in self.support_list:
            self.refresh_kline_data(refresh_cointype=coin)

    def parse_page(self,url):
        """从页面中提取出想要的数据，保存为一个DataFrame"""
        df = pd.DataFrame(columns = ['open','close','high','low','volume','date','MarketCap','pre_close',
                                    'date_week','p_change'])

        html = requests.get(url)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_tr = Soup.find_all('tr', class_ = 'text-right')

        # 每个tr中包含有含有具体数据的td标签
        td_preclose = np.nan
        for tr in all_tr[::-1]:
            tds = tr.find_all('td')
            # 每个td标签依次对应一个数据
            td_date_index = QsDateUtil.qs_cmformat_date(tds[0].string)
            td_date = QsDateUtil.date_str_to_int(td_date_index)
            td_open = tds[1].string
            td_high = tds[2].string
            td_low = tds[3].string
            td_close = tds[4].string
            td_volume = np.nan if tds[5].string == '-' else tds[5].string
            td_marketcap = np.nan if tds[6].string == '-' else tds[6].string
            td_date_week = QsDateUtil.week_of_date(td_date_index)
            td_p_change = np.nan if td_preclose is np.nan else round(((float(td_close)-float(td_preclose))/
                                                                        (float(td_preclose)))*100,3)
            insert_array = np.array([td_open,td_close,td_high,td_low,td_volume,td_date,td_marketcap,td_preclose,
                                    td_date_week,td_p_change])
            td_preclose = td_close
            df.loc[td_date_index] = insert_array
        return df

    def save_cache(self, datadf):
        """将获取的数据存储进cache文件夹，这里的datadf为DataFrame"""
        QsEnv.make_env_dir(QsEnv.g_project_cache_dir)
        datadf.fillna(np.nan)
        datastart = str(datadf.iloc[0]['date'])
        dataend = str(datadf.iloc[-1]['date'])
        filename = "qs" + self.targetcoin + "_" + datastart + "_" + dataend
        fullpath = os.path.join(QsEnv.g_project_cache_dir, filename)
        datadf.to_csv(fullpath, columns= datadf.columns, index=True, encoding='utf-8')
        print("[qiushui log] saving cache to " + fullpath)