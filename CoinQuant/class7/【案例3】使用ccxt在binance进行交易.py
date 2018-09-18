import ccxt
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# ccxt官方文档：https://github.com/ccxt/ccxt

# ccxt支持的交易所的id
# print(ccxt.exchanges)


# =====创建币安交易所
# 方法一
binance = ccxt.binance()
binance.apiKey = 'EwqLz2zfgL6Tx0uvYHPOyDdlfJKSqAUApU3vY51Kkt7XRD8poSwtDZTp4KTKCuKN'
binance.secret = '6fMHzWYGTsOS0Yc9Xcj636DgInBAlJxAegHmsnTPVatpiqsvz8Kzox1wVp66dmso'

# # 方法二
# binance = ccxt.binance(
#     {
#         'apiKey': 'EwqLz2zfgL6Tx0uvYHPOyDdlfJKSqAUApU3vY51Kkt7XRD8poSwtDZTp4KTKCuKN',
#         'secret': '6fMHzWYGTsOS0Yc9Xcj636DgInBAlJxAegHmsnTPVatpiqsvz8Kzox1wVp66dmso',
#     }
# )


# =====获取账户资产
balance = binance.fetch_balance()
print(balance)
exit()
# # 返回内容的数据结构：https://github.com/ccxt/ccxt/wiki/Manual#querying-account-balance
# print(balance['info'])  # 交易所原始返回内容
# print(balance['free'])  # 可以使用的资产数量
# print(balance['used'])  # 已经使用的资产数量，例如正在挂单交易的资产。
# print(balance['total'])  # 总资产数量

# print(balance['EOS'])  # EOS这个资产的数量
# print(balance['USDT'])  # USDT这个资产的数量


# =====下单交易
# 下单参数
# symbol = 'EOS/ETH'
# pirce = 0.03
# amount = 20

# 限价单
# order_info = binance.create_limit_buy_order(symbol, amount, pirce)  # 买单
# order_info = binance.create_limit_sell_order(symbol, amount, pirce)  # 卖单

# 市价单，市价单不需要输入价格
# order_info = binance.create_market_buy_order(symbol=symbol, amount=amount)  # 买单
# order_info = binance.create_market_sell_order(symbol=symbol, amount=amount)  # 卖单

# 返回内容的数据结构：https://github.com/ccxt/ccxt/wiki/Manual#placing-orders
# print(order_info['id'])
# print(order_info['info'])


# =====查询订单信息
# # 根据订单号查询订单信息
# order_info = binance.fetch_order(id='20508061', symbol='EOS/ETH')
# # 返回内容的数据结构：https://github.com/ccxt/ccxt/wiki/Manual#order-structure
# print(order_info)
# print(order_info['remaining'])
# print(order_info['status'])

# 根据交易对查询订单信息
# order_info = binance.fetch_orders(symbol='EOS/ETH', limit=10)  # limit参数控制返回最近的几条
# for i in order_info:
#     print(i['datetime'], i['status'])

# # 返回尚未成交的订单
# order_info = binance.fetch_open_orders(symbol='EOS/ETH', limit=10)  # limit参数控制返回最近的几条
# for i in order_info:
#     print(i['datetime'], i['status'])


# # =====撤单
# order_info = binance.cancel_order(id='20508061', symbol='EOS/ETH')
# print(order_info)
# order_info = binance.fetch_order(id='20508061', symbol='EOS/ETH')
# print(order_info['status'])
