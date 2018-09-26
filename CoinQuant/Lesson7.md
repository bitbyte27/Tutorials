# 第7课：交易所接口
## 目录
* [7.1 API接口概述](#71-API接口概述)
* [7.2 从各交易所获取实时数据](#72-从各交易所获取实时数据)
* [7.3 获取实时数据（更多案例）](#73-获取实时数据更多案例)
* [7.4 自动下单（上）](#74-自动下单上) 
* [7.5 自动下单（下）](#75-自动下单下) 

## 7.1 API接口概述
### https://coinmarketcap.com/
![](https://img3.doubanio.com/view/photo/l/public/p2534181313.jpg)
### https://coinmarketcap.com/rankings/exchanges/
### https://coinmarketcap.com/rankings/exchanges/reported/
![](https://img1.doubanio.com/view/photo/l/public/p2534181218.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534181145.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534181143.jpg)
### https://www.okex.com/
![](https://img1.doubanio.com/view/photo/l/public/p2534181207.jpg)
### https://github.com/bitbyte27/API-docs-OKEx.com
![](https://img3.doubanio.com/view/photo/l/public/p2534181161.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534181964.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534181938.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534181923.jpg)
### https://github.com/bitbyte27/API-docs-OKEx.com/blob/master/API-For-Futures-CN/%E5%90%88%E7%BA%A6%E4%BA%A4%E6%98%93REST%20API.md
![](https://img3.doubanio.com/view/photo/l/public/p2534181931.jpg)
### ticker
![](https://img3.doubanio.com/view/photo/l/public/p2534182416.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182414.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182412.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534182417.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182415.jpg)
### kline
![](https://img1.doubanio.com/view/photo/l/public/p2534182419.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182421.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182423.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182864.jpg)
### https://www.okb.com/market?product=ltc_btc
![](https://img3.doubanio.com/view/photo/l/public/p2534182862.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182852.jpg)
### trades
![](https://img3.doubanio.com/view/photo/l/public/p2534182855.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534182869.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182860.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534182849.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182866.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534182871.jpg)
### depth
![](https://img1.doubanio.com/view/photo/l/public/p2534183119.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534183118.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534183121.jpg)
### [更多的API数据](https://github.com/bitbyte27/API-docs-OKEx.com/blob/master/API-For-Futures-CN/%E5%90%88%E7%BA%A6%E4%BA%A4%E6%98%93REST%20API.md)
## 7.2 从各交易所获取实时数据
### url %s
![](https://img3.doubanio.com/view/photo/l/public/p2534311943.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534311936.jpg)
### urlopen,timeout
![](https://img3.doubanio.com/view/photo/l/public/p2534311952.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534311937.jpg)
* urlopen(url, timeout=15).read()

![](https://img1.doubanio.com/view/photo/l/public/p2534311949.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534311951.jpg)
### decode
* content = content.decode('utf-8')

![](https://img1.doubanio.com/view/photo/l/public/p2534311939.jpg)
### json.load
* json_data = json.loads(content)
* df = pd.DataFrame(json_data, dtype='float')

![](https://img3.doubanio.com/view/photo/l/public/p2534311946.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534413309.jpg)
### df.T
* df = df[['ticker']].T

![](https://img1.doubanio.com/view/photo/l/public/p2534413318.jpg)
### get_url_content
![](https://img3.doubanio.com/view/photo/l/public/p2534413310.jpg)
### get_list_ticker_from_okex
![](https://img1.doubanio.com/view/photo/l/public/p2534413307.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534636677.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534636681.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534636680.jpg)
### get_candle_from_okex
![](https://img3.doubanio.com/view/photo/l/public/p2534636684.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534636678.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534636683.jpg)
### 抓取报错，尝试次数
![](https://img1.doubanio.com/view/photo/l/public/p2534636689.jpg)
### get_candle_from_okex
![](https://img3.doubanio.com/view/photo/l/public/p2534636686.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534638802.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534638788.jpg)
### 重命名、时间转换（单位ms）、时区转换（东8区，GMT8）
![](https://img1.doubanio.com/view/photo/l/public/p2534638788.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534638796.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534638797.jpg)
## 7.3 获取实时数据（更多案例）
### time out 需要翻墙
![](https://img1.doubanio.com/view/photo/l/public/p2534638789.jpg)
### 翻墙后，还需要用浏览器伪装
![](https://img3.doubanio.com/view/photo/l/public/p2534638780.jpg)
* headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
* request = Request(url=url, headers=headers)
* content = urlopen(request, timeout=15).read()

![](https://img3.doubanio.com/view/photo/l/public/p2534638781.jpg)
### get_url_content2
![](https://img3.doubanio.com/view/photo/l/public/p2534638801.jpg)
### binance币安交易所
![](https://img1.doubanio.com/view/photo/l/public/p2534643148.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643150.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534643147.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643152.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534643157.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643156.jpg)
### huobipro火币交易所
![](https://img3.doubanio.com/view/photo/l/public/p2534643552.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643551.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643555.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534643554.jpg)
## 7.4 自动下单（上）
### ccxt官方文档：https://github.com/bitbyte27/ccxt
![](https://img3.doubanio.com/view/photo/l/public/p2535178575.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535178580.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535178563.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535178569.jpg)
### print(ccxt.exchanges)
![](https://img3.doubanio.com/view/photo/l/public/p2535178562.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535178576.jpg)
### www.binance.com ，设置API
![](https://img3.doubanio.com/view/photo/l/public/p2535179001.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535179018.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535179009.jpg)
### 创建币安交易所
* binance = ccxt.binance()
* binance.apiKey = ''
* binance.secret = ''

![](https://img3.doubanio.com/view/photo/l/public/p2535179014.jpg)
### 获取账户资产
* balance = binance.fetch_balance()

![](https://img3.doubanio.com/view/photo/l/public/p2535179006.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535179013.jpg)
* balance['info']  # 交易所原始返回内容。

![](https://img1.doubanio.com/view/photo/l/public/p2535179007.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535179000.jpg)
* balance['free']  # 可以使用的资产数量。
* balance['used']  # 已经使用的资产数量，例如正在挂单交易的资产。
* balance['total']  # 总资产数量。

![](https://img1.doubanio.com/view/photo/l/public/p2535179638.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535179636.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535179634.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535179639.jpg)
* balance['EOS']  # EOS这个资产的数。
* balance['USDT']  # USDT这个资产的数量。

![](https://img3.doubanio.com/view/photo/l/public/p2535179643.jpg)
### 下单交易
* symbol = 'EOS/ETH'
* pirce = 0.03
* amount = 20

![](https://img3.doubanio.com/view/photo/l/public/p2535179650.jpg)
### 查看交易所实时下单情况
![](https://img3.doubanio.com/view/photo/l/public/p2535179646.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535179647.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535179651.jpg)
### 限价单
* order_info = binance.create_market_buy_order(symbol=symbol, amount=amount)  # 买单
![](https://img3.doubanio.com/view/photo/l/public/p2535180242.jpg)
* 因为没有金额，所以不能挂单，会报错

![](https://img1.doubanio.com/view/photo/l/public/p2535180247.jpg)
* order_info = binance.create_market_sell_order(symbol=symbol, amount=amount)  # 卖单

![](https://img1.doubanio.com/view/photo/l/public/p2535180249.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535180244.jpg)
* 修改数量、金额后再挂单
![](https://img3.doubanio.com/view/photo/l/public/p2535180243.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535180241.jpg)
## 7.5 自动下单（下）
![]()
![]()
![]()
![]()
![]()
![]()
> To be continue……
