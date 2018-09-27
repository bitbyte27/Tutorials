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

> To be continue……
