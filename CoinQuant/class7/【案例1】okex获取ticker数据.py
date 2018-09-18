from urllib.request import urlopen, Request
import json
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# 抓取交易对的symbol
symbol = 'ltc_usdt'

# 构建url
# url = 'https://www.okex.com/api/v1/ticker.do?symbol=' + symbol
url = 'https://www.okex.com/api/v1/ticker.do?symbol=%s' % symbol

# # 抓取数据
# content = urlopen(url=url, timeout=15).read()
# content = content.decode('utf-8')

# 抓取数据，带有浏览器伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
request = Request(url=url, headers=headers)
content = urlopen(request, timeout=15).read()
content = content.decode('utf-8')

# 将数据转化为dataframe
json_data = json.loads(content)
df = pd.DataFrame(json_data, dtype='float')

# 对df进行处理
df = df[['ticker']].T

print(df)
