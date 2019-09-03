# -*- encoding:utf-8 -*-

import os
from os import path
import logging

#logging.basicConfig(level=logging.WARNING,format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊ 数据目录 start ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
root_drive = path.expanduser('~')
"""qsq数据缓存主目录文件夹"""
g_project_root = path.join(root_drive, 'qsq')
"""qsq数据文件夹 ~/qsq/data"""
g_project_data_dir = path.join(g_project_root, 'data')
"""qsq日志文件夹 ~/qsq/log"""
g_project_log_dir = path.join(g_project_root, 'log')
"""qsq数据库文件夹 ~/qsq/db"""
g_project_db_dir = path.join(g_project_root, 'db')
"""qsq缓存文件夹 ~/qsq/cache"""
g_project_cache_dir = path.join(g_project_data_dir, 'cache')

def make_env_dir(file_path):
    folder = os.path.exists(file_path)
    if not folder:
        os.makedirs(file_path)
        print(" new folder: " + file_path)