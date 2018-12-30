# 第8课：择时策略之回测
## 目录
* [8.1 产生交易信号](#81-产生交易信号)
* [8.2 计算资金曲线准备工作](#82-计算资金曲线准备工作)
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
* 周期转换还可参考：http://bbs.pinggu.org/thread-3668396-1-1.html

![](https://img3.doubanio.com/view/photo/l/public/p2542084203.jpg)
<br>
[极简方法将日线数据转为周线、月线或其他周期](class8/极简方法将日线数据转为周线、月线或其他周期.py)
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
### 找出做多信号
* condition1 = df['close'] > df['upper']  # 当前K线的收盘价 > 上轨。
* condition2 = df['close'].shift(1) <= df['upper'].shift(1)  # 之前K线的收盘价 <= 上轨。
* df.loc[condition1 & condition2, 'signal_long'] = 1  # 将产生做多信号的那根K线的signal设置为1，1代表做多。

![](https://img1.doubanio.com/view/photo/l/public/p2535704189.jpg)
### 找出做多平仓信号
* condition1 = df['close'] < df['median']  # 当前K线的收盘价 < 中轨。
* condition2 = df['close'].shift(1) >= df['median'].shift(1)  # 之前K线的收盘价 >= 中轨。
* df.loc[condition1 & condition2, 'signal_long'] = 0  # 将产生平仓信号当天的signal设置为0，0代表平仓。

![](https://img3.doubanio.com/view/photo/l/public/p2535704180.jpg)
### 找出做空信号
* condition1 = df['close'] < df['lower']  # 当前K线的收盘价 < 下轨。
* condition2 = df['close'].shift(1) >= df['lower'].shift(1)  # 之前K线的收盘价 >= 下轨。
* df.loc[condition1 & condition2, 'signal_short'] = -1  # 将产生做空信号的那根K线的signal设置为-1，-1代表做空。
### 找出做空平仓信号
* condition1 = df['close'] > df['median']  # 当前K线的收盘价 > 中轨。
* condition2 = df['close'].shift(1) <= df['median'].shift(1)  # 之前K线的收盘价 <= 中轨。
* df.loc[condition1 & condition2, 'signal_short'] = 0  # 将产生平仓信号当天的signal设置为0，0代表平仓。

![](https://img1.doubanio.com/view/photo/l/public/p2535704187.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535704176.jpg)
### 合并做多做空信号，去除重复信号
* df.drop_duplicates(subset=['signal_long', 'signal_short'], inplace=True)

![](https://img3.doubanio.com/view/photo/l/public/p2535704183.jpg)
* df['signal'] = df[['signal_long', 'signal_short']].sum(axis=1, skipna=True)

![](https://img1.doubanio.com/view/photo/l/public/p2535704177.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535704184.jpg)
* temp = df[df['signal'].notnull()][['signal']]  # 删除空值

![](https://img3.doubanio.com/view/photo/l/public/p2535704185.jpg)
* temp = temp[temp['signal'] != temp['signal'].shift(1)]  # 寻找与上一行不同的行，删除重复信号。

![](https://img3.doubanio.com/view/photo/l/public/p2535704174.jpg)

* df['signal'] = temp['signal']

![](https://img3.doubanio.com/view/photo/l/public/p2535705960.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535705973.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2535705952.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535705979.jpg)
* df.drop(['median', 'std', 'upper', 'lower', 'signal_long', 'signal_short'], axis=1, inplace=True)

![](https://img1.doubanio.com/view/photo/l/public/p2535705969.jpg)
### 由signal计算出实际的每天持有仓位
### signal的计算运用了收盘价，是每根K线收盘之后产生的信号，到第二根开盘的时候才买入，仓位才会改变。
* df['pos'] = df['signal'].shift()

![](https://img1.doubanio.com/view/photo/l/public/p2535705977.jpg)
* df['pos'].fillna(method='ffill', inplace=True)

![](https://img3.doubanio.com/view/photo/l/public/p2535705961.jpg)
* df['pos'].fillna(value=0, inplace=True)  # 将初始行数的position补全为0。

![](https://img3.doubanio.com/view/photo/l/public/p2535705964.jpg)
### 将数据存入hdf文件中
* df.to_hdf('/Users/jxing/Desktop/coin_quant_class/data/class8/eth_bolling_signal.h5', key='all_data', mode='w')

![](https://img1.doubanio.com/view/photo/l/public/p2535705967.jpg)
## 8.2 计算资金曲线准备工作
### 导入数据
* df = pd.read_hdf('/Users/jxing/Desktop/coin_quant_class/data/class8/eth_bolling_signal.h5', key='all_data')

![](https://img3.doubanio.com/view/photo/l/public/p2535719966.jpg)
### 根据pos计算资金曲线
### 计算涨跌幅
* df['change'] = df['close'].pct_change(1)  # 根据收盘价计算涨跌幅。

![](https://img3.doubanio.com/view/photo/l/public/p2535719963.jpg)
* df['buy_at_open_change'] = df['close'] / df['open'] - 1  # 从今天开盘买入，到今天收盘的涨跌幅。
* df['sell_next_open_change'] = df['open'].shift(-1) / df['close'] - 1  # 从今天收盘到明天开盘的涨跌幅。

![](https://img3.doubanio.com/view/photo/l/public/p2535719960.jpg)
* df.at[len(df) - 1, 'sell_next_open_change'] = 0  # 令最后一个为零。

![](https://img3.doubanio.com/view/photo/l/public/p2535719955.jpg)
### 选取时间段
* df = df[df['candle_begin_time'] >= pd.to_datetime('2017-01-01')]
* df.reset_index(inplace=True, drop=True)

![](https://img3.doubanio.com/view/photo/l/public/p2535719956.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2535719958.jpg)

![]()
![]()
![]()
![]()
![]()
![]()
![]()
![]()
> To be continue……
