'''
程序入口
'''
import sys
import os
from os import system
import getpass

# import win32com.client
import msoffcrypto
import io
import pandas as pd
from termcolor import colored

from lib import comm

def StartedTheEngine():
    exists_xlsx = os.path.normpath(os.path.join(comm.BASE_PATH, 'inventory', 'devices.xlsx'))
    if os.path.exists(exists_xlsx):
        os.system(f"python {comm.BASE_PATH}/func/func_list.py")
        sys.exit()
    else:
        print('-' * 42)
        print(colored('请检查当前文件夹inventory中devices.xlsx文件', 'blue'))
        sys.exit()

# 命令行窗口标题
system("title Python-NetOps_2.0_beta")

if __name__ == "__main__":

    StartedTheEngine()
