"""
此为多行注释方式
author: xingbuxing
date: 2018年01月11日
功能：本程序主要介绍python的常用的数据类型，以及计算符号。希望以后大家只要看这个程序，就能回想起相关的基础知识。
"""

# ===注释的用法
# 在每一行的开头，加上#，是对该行进行单行注释
# print('hello world')  # 行末注释，在一句程序的末尾，一般用来解释这句话。注意空格。

# control + / 多行同时注释或取消注释（mac上是command + /）。
# 尝试同时取消注释或注释下面三行代码
# print('hello world')
# print('hello world')
# print('hello world')


# ===数字,num
# int类型的整数
# bfx_coin_num = 23  # 整数，BITFINEX交易所有23个币正在交易
# print(bfx_coin_num, type(bfx_coin_num))  # type()函数的作用是输出变量的类型
# float类型的浮点数
# eth_usd_price = 1231.7  # 浮点数，以太坊价格1231.7
# print(eth_usd_price, type(eth_usd_price))
# eth_btc_price = .09  # 小数点之前的0可以省略，.09和0.09是一样的。
# print(eth_btc_price, type(eth_btc_price))
# btc_change = -0.137  # 负数的表示方式，涨跌幅-13.7%
# print(btc_change, type(btc_change))
# btc_market_capital = 2.33E11  # 比特币市值，可以使用科学技术发来表示很大的数字
# print(btc_market_capital, type(btc_market_capital))


# ===字符串,string
# 字符串：以单引号’，双引号”，三引号’’’开始，同样符号结束
# symbol = 'btcusd'
# print(symbol, type(symbol))
# symbol_name = "比特币/美元"
# print(symbol_name, type(symbol_name))


# ===布尔值：只有两个，True和False。大小写敏感
# print(True, False, type(True))


# ===空值：只有一个，None。大小写敏感。表示没有值的值
# print(None, type(None))


# ===变量名称
# 变量需要名称
# 不要使用a、b、c、aa等无意义的变量名
# 取名规则：首字母需要是字母或下划线，其余部分可以是字母，下划线和数字


# ===算术符号, + - * / %
# 以加法为例子，可以把下面的加号变成- * /其他符号。
# bfx_coin_num = 23  # 现有23个币正在交易
# new_coin_num = 7  # 新增币7个
# all_coin_num = bfx_coin_num + new_coin_num  # 全部股票共有多少只？
# print(all_coin_num)

# % 取余数的操作
# print(9 % 15)

# ** 乘方操作
# print(3 ** 4)

# 自运算的快速写法
# bfx_coin_num = 23
# bfx_coin_num += 7  # 效果等同于：bfx_coin_num = bfx_coin_num + 7。可以把加号变成- * /等其他符号。
# print(bfx_coin_num)

# 算术符号可以连接两个不同类型的变量
# print(23 + 7.5)
# print(3 * 'abc')
# print(3 + 'abc')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'


# ===比较运算> < >= <= == !=
# num1 = 10
# num2 = 20
# print(num1 > num2)  # 判断num1是否大于num2，输出结果是布尔变量
# print(num1 >= num2)  # 判断num1是否大于等于num2
# print(num1 == num2)  # 判断num1是否等于num2
# print(num1 != num2)  # 判断num1是否不等于于num2


# ===布尔运算and or & |
# and &，两者都为真，才是真
# print((2 > 1) & (2 != 1))  # 两者都是True，输出结果就是True
# print(2 > 1 & 2 == 1)  # 其中有一个为False，输出结果就是False

# or | 至少一个为真，就是真
# print((2 > 1) | (2 == 1))  # 其中有一个为True，输出结果就是True
