import ccxt
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# =====创建bitfinex交易所
bitfinex = ccxt.bitfinex()
bitfinex.apiKey = 'ANYU4oeRdxbqSuSU9VcICQiob0ysEB69RtLOygF9sbR'
bitfinex.secret = 'PMTTUkrncy6SWNFgMYQkqA8YAtBmY6oXm8YCuUpNw9W'


# =====获取bitfinex账户资产
# balance_exchange = bitfinex.fetch_balance()  # 获取exchange账户资产
# print(balance_exchange['info'])
# print(balance_exchange['free'])
# print(balance_exchange['used'])
# print(balance_exchange['total'])

# balance_margin = bitfinex.fetch_balance({'type': 'trading'})  # 获取margin账户资产
# print(balance_margin['USD'])  # USD这个资产的数量


# =====下单交易
# 下单参数
# symbol = 'BTC/USD'
# pirce = 3000
# amount = 10

# 下单类型：
# market：margin交易市价单
# limit：margin交易限价单
# exchange market：exchange交易市价单
# exchange limit：exchange交易限价单

# 限价单
# order_info = bitfinex.create_limit_buy_order(symbol, amount, pirce, {'type': 'limit'})  # margin买单
# order_info = bitfinex.create_limit_sell_order(symbol, amount, pirce, {'type': 'limit'})  # margin卖单

# 市价单，市价单不需要输入价格
# order_info = bitfinex.create_market_buy_order(symbol, amount, {'type': 'market'})  # margin买单
# order_info = bitfinex.create_market_sell_order(symbol, amount, {'type': 'market'})  # margin买单

# 返回内容的数据结构：https://github.com/ccxt/ccxt/wiki/Manual#placing-orders
# print(order_info['id'])
# print(order_info['info'])


# =====查询订单信息
# # # 根据订单号查询订单信息
# order_info = bitfinex.fetch_order(id='10210315895', symbol='BTC/USD')
# # # 返回内容的数据结构：https://github.com/ccxt/ccxt/wiki/Manual#order-structure
# print(order_info)
# print(order_info['remaining'])
# print(order_info['status'])

# # 根据交易对查询订单信息
# bitfinex没有fetchOrders这个方法
# print(bitfinex.has)
# print(bitfinex.has['fetchOrders'])

# # 返回尚未成交的订单
# order_info = bitfinex.fetch_open_orders(symbol='BTC/USD', limit=10)  # limit参数控制返回最近的几条
# for i in order_info:
#     print(i['datetime'], i['status'], i['id'])
#     print(i)


# # =====撤单
# order_info = bitfinex.cancel_order(id='10210315895', symbol='BTC/USD')
# print(order_info)
# order_info = bitfinex.fetch_order(id='10210315895', symbol='BTC/USD')
# print(order_info['status'])
