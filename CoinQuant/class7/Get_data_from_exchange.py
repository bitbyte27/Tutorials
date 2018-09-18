from urllib.request import urlopen, Request
import json
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# ===抓取数据
def get_url_content(url, max_try_number=5):
    try_num = 0
    while True:
        try:
            return urlopen(url, timeout=15).read().strip()
        except Exception as http_err:
            print(url, "抓取报错", http_err)
            try_num += 1
            if try_num >= max_try_number:
                print("尝试失败次数过多，放弃尝试")
                return None


# ===抓取数据，带有浏览器伪装
def get_url_content2(url, max_try_number=5):
    try_num = 0
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            request = Request(url=url, headers=headers)
            content = urlopen(request, timeout=15).read()
            return content
        except Exception as http_err:
            print(url, "抓取报错", http_err)
            try_num += 1
            if try_num >= max_try_number:
                print("尝试失败次数过多，放弃尝试")
                return None


# ===okex
# 获取ticker数据
def get_list_ticker_from_okex(symbol_list=['btc_usdt', 'ltc_usdt']):

    # 创建一个空的df
    df = pd.DataFrame()

    # 遍历每一个symbol
    for symbol in symbol_list:
        # 构建url
        url = 'https://www.okex.com/api/v1/ticker.do?symbol=%s' % symbol
        # 抓取数据
        content = get_url_content2(url, 5)
        if content is None:  # 当返回内容为空的时候，跳过本次循环
            continue

        # 将数据转化为dataframe
        json_data = json.loads(content.decode("utf-8"))
        _df = pd.DataFrame(json_data, dtype='float')
        _df = _df[['ticker']].T
        _df['symbol'] = symbol

        # 合并数据到df中
        df = df.append(_df, ignore_index=True)

    # 对df进行最后整理
    df = df[['symbol', 'last', 'buy', 'sell', 'high', 'low', 'vol']]

    return df


# 获取candle数据
def get_candle_from_okex(symbol='ltc_usdt', kline_type='1min'):

    # 构建url
    url = 'https://www.okex.com/api/v1/kline.do?symbol=%s&type=%s' % (symbol, kline_type)

    # 抓取数据
    content = get_url_content2(url)
    if content is None:  # 当返回内容为空的时候，跳过本次循环
        return pd.DataFrame()

    # 将数据转化为dataframe
    json_data = json.loads(content.decode("utf-8"))
    df = pd.DataFrame(json_data, dtype='float')

    # 整理dataframe
    df.rename(columns={0: 'candle_begin_time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'}, inplace=True)
    df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'], unit='ms')
    df['candle_begin_time_GMT8'] = df['candle_begin_time'] + pd.Timedelta(hours=8)

    return df


df = get_list_ticker_from_okex(symbol_list=['btc_usdt', 'ltc_usdt', 'eth_usdt'])
print(df)

df = get_candle_from_okex(symbol='btc_usdt', kline_type='30min')
print(df)

