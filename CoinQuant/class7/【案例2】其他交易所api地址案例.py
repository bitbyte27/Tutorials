from urllib.request import urlopen, Request
import json
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行



# ===okex交易所
url = 'https://www.okex.com/api/v1/ticker.do?symbol=ltc_usdt'  # tick数据
# url = 'https://www.okex.com/api/v1/kline.do?symbol=btc_usdt&type=30min'  # k线数据

# ===binance交易所
# url = 'https://api.binance.com/api/v1/ticker/24hr'  # tick数据
# url = 'https://api.binance.com/api/v1/klines?symbol=LTCBTC&interval=1h'  # k线数据

# ===huobipro交易所
# url = 'https://api.huobipro.com/market/detail/merged?symbol=btcusdt'  # tick数据
# url = 'https://api.huobipro.com/market/history/kline?symbol=btcusdt&period=1min'  # k线数据

# # 抓取数据
# content = urlopen(url=url, timeout=15).read()
# content = content.decode('utf-8')

# 抓取数据，带有浏览器伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
request = Request(url=url, headers=headers)
content = urlopen(request, timeout=15).read()
content = content.decode('utf-8')

print(content)
