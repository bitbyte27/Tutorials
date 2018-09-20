# 第7课：交易所接口
## 目录
* [7.1 API接口概述](#71-API接口概述)
* [7.2 从各交易所获取实时数据](#72-从各交易所获取实时数据)

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
![](https://img1.doubanio.com/view/photo/l/public/p2534311949.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534311951.jpg)
### decode
![](https://img1.doubanio.com/view/photo/l/public/p2534311939.jpg)
### json.load
![](https://img3.doubanio.com/view/photo/l/public/p2534311946.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534413309.jpg)
### df.T
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
![]()
![]()
> To be continue……
