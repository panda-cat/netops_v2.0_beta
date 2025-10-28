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
from termcolor import colored

from lib import comm
from func import func_list

def StartedTheEngine():
    exists_xlsx = os.path.normpath(os.path.join(comm.BASE_PATH, 'inventory', 'devices.xlsx'))
    if os.path.exists(exists_xlsx):
        # os.system(f"python {comm.BASE_PATH}/func/func_list.py") # <--- 2. 删除这一行
        # sys.exit()                                              # <--- 3. 删除这一行
        func_list.run()                                         # <--- 4. 添加这一行，直接调用
        sys.exit()                                              # <--- 5. 在调用后退出
    else:
        print('-' * 42)
        print(colored('请检查当前文件夹inventory中devices.xlsx文件', 'blue'))
        sys.exit()

# 命令行窗口标题
system("title Python-NetOps_2.0_beta")

if __name__ == "__main__":
    StartedTheEngine()
