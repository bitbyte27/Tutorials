"""
火币有多少交易币对

读取k线数据

"""
from urllib.request import urlopen,Request
import json
import pandas as pd
import numpy as np

pd.set_option('expand_frame_repr', False) #当列太多时不换行

def get_url_content(url, max_try_number=5):
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


def get_list_symbols_from_huobi():

    # 创建一个空的df
    df = pd.DataFrame()

    # 构建url
    url = 'https://api.huobipro.com/v1/common/symbols'

    # 设置header
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # request = Request(url=url, headers=headers)
    content = get_url_content(url, 5)
    # print(content)
    # print(type(content))

    # 转换格式
    # content = content.decode("utf-8")
    # print(content)
    # print(type(content))
    json_data = json.loads(content.decode("utf-8"))
    json_data = json_data['data']
    # print(json_data)
    # print(type(json_data))
    df = pd.DataFrame(json_data, dtype='str')
    # print(df)
    # print(type(df))

    # 取某几列
    df = df[['base-currency', 'quote-currency', 'symbol-partition']]

    # 新增一列
    df['base-quote'] = df['base-currency'] + df['quote-currency']
    df['resource'] = 'huobi'

    # 对df进行整理
    df = df[['base-currency','quote-currency','base-quote','symbol-partition','resource']]

    symbol_list = list(df['base-quote'])
    # 存储数据
    # df.to_csv('symbols.csv', index=False)

    return symbol_list



# 获取k线数据
def get_candle_from_huobi(period='1day',size=1):
    symbol_list = get_list_symbols_from_huobi()


    # 创建一个空的df
    df = pd.DataFrame()

    # 遍历每一个symbol
    for symbol in symbol_list[:20]:
        print(symbol)
        # 构建url
        url = 'https://api.huobipro.com/market/history/kline?period=%s&size=%s&symbol=%s' % (period,size,symbol)
        # print(url)
        # exit()
        # 抓取数据
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # request = Request(url=url, headers=headers)
        content = get_url_content(url)

        if content is None:
            continue
        # print(content)
        # print(type(content))
        # exit()
        # 将数据转换成df
        json_data = json.loads(content.decode("utf-8"))

        # print(json_data['data'])
        # exit()
        _df = pd.DataFrame(json_data['data'], dtype='float')
        # _df = _df.T
        # print(_df)
        _df['symbol'] = symbol
        # print(_df)
        df = df.append(_df,ignore_index=0)
        # print(df)
        #exit()
    # 对df进行整理
    df = df[['symbol','id','high','low','open','close','vol']]
    # print(df)
    # 重命名
    df.rename(columns={'id':'time'},inplace=True)
    # print(df)
    df['time'] = pd.to_datetime(df['time'],unit='s') + pd.Timedelta(hours=8)

    return df


df = get_candle_from_huobi(period='1day', size=1)

df.to_csv('all_kline.csv',index=False)

