"""
程序开头注释
author: xingbuxing
date: 2018年01月11日
功能：本程序主要介绍python的异常处理功能
"""

# =====异常处理
# 语法
"""
try:
    执行相关语句1
except:
    执行相关语句2
else:
    执行相关语句3
"""

# 说明
"""
1. 先尝试执行相关语句1
2. 若在执行语句1的过程中报错，那么执行相关语句2
3. 若在执行语句1的过程中没有报错，那么执行相关语句3
"""


# # =====异常处理的一个例子
# import time  # 导入系统库time，可以使用一些系统级别的函数
#
#
# def buy_one_stock(stock_name='sh600000'):  # 参数为股票名
#     """
#     此程序用于下单买入某个股票，但是买入过程中，程序有50%的概率报错。
#     """
#     import random
#     random = random.random()
#     if random >= 0.5:
#         return
#     else:
#         raise ValueError('程序报错！')
# # buy_one_stock()
#
# max_try_num = 5
# tyr_num = 0
# while True:
#     try:  # 尝试做以下事情
#         buy_one_stock()
#     except:  # 如果因为各种原因报错
#         print '警告！下单出错，停止1秒再尝试'
#         tyr_num += 1
#         time.sleep(1)
#         if tyr_num > max_try_num:
#             print '超过最大尝试次数，下单失败'
#             # 此处需要执行相关程序，通知某些人
#             break
#     else:  # 如果没有报错
#         print '下单成功了'
#         break
#
#


