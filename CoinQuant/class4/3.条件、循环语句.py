"""
程序开头注释
author: xingbuxing
date: 2018年01月11日
功能：本程序主要介绍python的条件语句、循环语句
"""


# =====条件语句介绍
# 条件语句语法如下：
"""
if 条件A（结果为布尔值，true或者False）:
    执行相关操作1（需要使用tab缩进）
    ......

elif 条件B（结果为布尔值，true或者False）:
    执行相关操作2
    ......

else:
    执行相关操作3
"""

# 条件语句解释说明如下：
"""
1. 若条件A为True，那么执行相关操作1，程序结束
2. 若条件A为False，那么判断条件B，若条件B为True，那么执行相关操作2，程序结束
3. 若条件A为False，那么判断条件B，若条件B为False，那么执行相关操作3，程序结束
"""

# 条件语句示例：根据symbol代码，判断币的计价单位
# symbol = 'xrpusd'  # 尝试将symbol改成'xrpbtc'，'xrpeth', 'xrpbnb'看相关结果。
# if symbol.endswith('usd'):
#     print(symbol, '以美元计价')
# elif symbol.endswith('btc'):
#     print(symbol, '以比特币计价')
# elif symbol.endswith('eth'):
#     print(symbol, '以以太坊计价')
# else:
#     print(symbol, '不知道以什么计价')


# =====for循环语句介绍
# for循环是最常用的循环语句

# 案例1：循环输出['btcusd', 'ethusd', 'xrpusd']中的结果
# for symbol in ['btcusd', 'ethusd', 'xrpusd']:
#     print(symbol)

# 案例2：计算1+2+3+……+10
# sum_num = 0  # 用于存储计算的结果
# for i in range(10 + 1):
#     sum_num += i  # 此处需要使用tab按键进行缩进
#     print i, sum_num

# 案例3：批量判断币的计价单位
# symbol_list = ['btcusd', 'xrpbtc', 'xrpusd', 'xrpeth', 'ethusd', 'xrpbnb']
# for symbol in symbol_list:
#     if symbol.endswith('usd'):
#         print(symbol, '以美元计价')
#         continue
#     if symbol.endswith('btc'):
#         print(symbol, '以比特币计价')
#         continue
#     if symbol.endswith('eth'):
#         print(symbol, '以以太坊计价')
#         continue
#     print(symbol, '不知道以什么计价')


# =====while语句
# while语句语法如下：
"""
while 条件A:
    执行相关操作1（需要使用tab缩进）
    ......
"""

# 条件语句解释说明如下：
"""
1. 判断条件A，若条件A为False，那么程序结束。
2. 判断条件A，若条件A为True，那么执行相关操作1。
3. 然后再次判断条件A，重复上面的步骤
"""

# while语句案例1：计算1+2+3+……+10
# num = 1
# max_num = 10
# sum_num = 0  # 存储计算结果
# while num <= max_num:
#     sum_num += num
#     num += 1
#     print sum_num
#
# # while语句案例2：计算1+2+3+……+10
# num = 1
# max_num = 10
# sum_num = 0
# while True:
#     sum_num += num
#     num += 1
#     print sum_num, num
#     if num == max_num+1:
#         break
