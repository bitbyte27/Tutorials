# 第8课：择时策略-回测
## 目录
* [8.1 产生交易信号]()
* [8.2 计算资金曲线准备工作]()
* [8.3 计算资金曲线]()
* [8.4 爆仓情况处理]()
* [8.5 寻找最优参数]()

## 8.1 产生交易信号
### 导入数据
* df = pd.read_hdf('class8/eth_1min_data.h5', key='all_data')
### 转换为其他分钟数据
* rule_type = '15T'
* period_df = df.resample(rule=rule_type, on='candle_begin_time', label='left', closed='left').agg(……)
* period_df.dropna(subset=['open'], inplace=True)  # 去除一天都没有交易的周期
* period_df = period_df[period_df['volume'] > 0]  # 去除成交量为0的交易周期
* period_df.reset_index(inplace=True)
* df = period_df[['candle_begin_time', 'open', 'high', 'low', 'close', 'volume']]

![](https://img3.doubanio.com/view/photo/l/public/p2535187912.jpg)
* df = df[df['candle_begin_time'] >= pd.to_datetime('2017-01-01')]
* df.reset_index(inplace=True, drop=True)

![](https://img3.doubanio.com/view/photo/l/public/p2535187851.jpg)
### 产生交易信号：布林线策略
* 布林线中轨：n天收盘价的移动平均线
* 布林线上轨：n天收盘价的移动平均线 + m * n天收盘价的标准差
* 布林线上轨：n天收盘价的移动平均线 - m * n天收盘价的标准差
* 当收盘价由下向上穿过上轨的时候，做多；然后由上向下穿过下轨的时候，平仓。
* 当收盘价由上向下穿过下轨的时候，做空；然后由下向上穿过上轨的时候，平仓。

![](https://img3.doubanio.com/view/photo/l/public/p2535257823.jpg)
### 计算指标
* n = 100
* m = 2
### 计算均线
* df['median'] = df['close'].rolling(n, min_periods=1).mean()

![](https://img3.doubanio.com/view/photo/l/public/p2535257855.jpg)
### 计算上轨、下轨道
* df['std'] = df['close'].rolling(n, min_periods=1).std(ddof=0)  # ddof代表标准差自由度。
* df['upper'] = df['median'] + m * df['std']
* df['lower'] = df['median'] - m * df['std']

![](https://img1.doubanio.com/view/photo/l/public/p2535257899.jpg)

![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()

> To be continue……
