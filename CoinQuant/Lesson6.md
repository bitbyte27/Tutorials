# 第6课：Pandas高阶操作
## 目录
* [6.1 批量导入数据](#61-批量导入数据)
* [6.2 HDF存取数据](#62-hdf存取数据)
* [6.3 转变K线数据周期](#63-转变k线数据周期)
* [6.4 groupby分组](#64-groupby分组)

## 6.1 批量导入数据
### 遍历文件
* import os
* pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
* 系统自带函数os.walk，用于遍历文件夹中的所有文件，os是python自带的系统库。

![](https://img1.doubanio.com/view/photo/l/public/p2533961199.jpg)
* for root, dirs, files in os.walk('/Users/jxing/Desktop/coin_quant_class/data'):
* root输出文件夹，dirs输出root下所有的文件夹，files输出root下的所有的文件。
* print('root:', root)
* print('dirs:', dirs)
* print('files:', files)

![](https://img1.doubanio.com/view/photo/l/public/p2533961187.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533961172.jpg)
### 批量读取文件名称
* file_list = []
* for root, dirs, files in os.walk('/Users/jxing/Desktop/coin_quant_class/data/class6'):
* 当files不为空的时候
* if files:
* print(files)

![](https://img3.doubanio.com/view/photo/l/public/p2533961196.jpg)
* for f in files:
* if f.endswith('.csv'):
* file_list.append(f)

![](https://img3.doubanio.com/view/photo/l/public/p2533961191.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533961184.jpg)
### 遍历文件名，批量导入数据
* all_data = pd.DataFrame()
* for file in sorted(file_list):
* print(file)
* 导入数据
* df = pd.read_csv('/Users/jxing/Desktop/coin_quant_class/data/class6/BITFINEX/EOSUSD/' + file,
* skiprows=1,
* parse_dates=['candle_begin_time'])

![](https://img3.doubanio.com/view/photo/l/public/p2533961185.jpg)
* 合并数据
* all_data = all_data.append(df, ignore_index=True)  # 注意此时若一下子导入很多文件，可能会内存溢出

![](https://img3.doubanio.com/view/photo/l/public/p2533961174.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533961198.jpg)
### 对数据进行排序
* all_data.sort_values(by=['candle_begin_time'], inplace=True)

![](https://img3.doubanio.com/view/photo/l/public/p2533961210.jpg)
### 将数据存入csv文件中
![](https://img3.doubanio.com/view/photo/l/public/p2533961211.jpg)

## 6.2 HDF存取数据
### 将数据存入hdf文件中
* all_data.to_hdf('.h5', key='all_data', mode='w')

![](https://img1.doubanio.com/view/photo/l/public/p2534180347.jpg)
### 从hdf中读取文件
* all_data = pd.read_hdf(.h5', key='all_data')

![](https://img3.doubanio.com/view/photo/l/public/p2534180332.jpg)
### 创建hdf文件
* h5_store = pd.HDFStore('eos_data.h5', mode='w')

![](https://img3.doubanio.com/view/photo/l/public/p2534180335.jpg)
### 批量导入并且存储数据
* for file in sorted(file_list):
* date = file.split('_')[2]
* print(date)

![](https://img3.doubanio.com/view/photo/l/public/p2534178845.jpg)
### 导入数据
* df = pd.read_csv('/Users/jxing/Desktop/coin_quant_class/data/class6/BITFINEX/EOSUSD/' + file,
* skiprows=1,
* parse_dates=['candle_begin_time'])
                     
![](https://img3.doubanio.com/view/photo/l/public/p2534179421.jpg)
### 存储数据到hdf
* h5_store['eos_'+date] = df

![](https://img3.doubanio.com/view/photo/l/public/p2534178881.jpg)
### 关闭hdf文件
* h5_store.close()
### 读取hdf数据
### 创建hdf文件
* h5_store = pd.HDFStore('eos_data.h5', mode='r')
* w：写入
* r：读取

![](https://img3.doubanio.com/view/photo/l/public/p2534179411.jpg)
### h5_store中的key
* print(h5_store.keys())

![](https://img3.doubanio.com/view/photo/l/public/p2534178851.jpg)
### 读取某个key指向的数据
* print(h5_store.get('eos_20170701'))

![](https://img3.doubanio.com/view/photo/l/public/p2534178883.jpg)
* print(h5_store['eos_20180301'])

![](https://img1.doubanio.com/view/photo/l/public/p2534178858.jpg)
### 关闭hdf文件
* h5_store.close()

![](https://img1.doubanio.com/view/photo/l/public/p2534178979.jpg)

## 6.3 转变K线数据周期
![](https://img1.doubanio.com/view/photo/l/public/p2534413438.jpg)
### 从hdf中读取1分钟数据
* df = pd.read_hdf('/Users/jxing/Desktop/coin_quant_class/data/class6/eos_1min_data.h5', key='all_data')
### 选取某一时间段
* df = df[df['candle_begin_time'] >= pd.to_datetime('2017-03-01')]
* print(df.head(10))

![](https://img3.doubanio.com/view/photo/l/public/p2534413442.jpg)
### 《数据周线转换示意图》

![](https://img3.doubanio.com/view/photo/l/public/p2534413435.jpg)
### 第一种方法：将1分钟数据转为5分钟数据
### 将candle_begin_time设定为index
* df.set_index('candle_begin_time', inplace=True)

![](https://img3.doubanio.com/view/photo/l/public/p2534413433.jpg)
### 周期转换方法：resample
* rule_type = '5T'  # rule='5T'：意思是5分钟，意味着转变为5分钟数据
* period_df = df[['close']].resample(rule=rule_type).last()  # last：取这5分钟的最后一行数据

![](https://img3.doubanio.com/view/photo/l/public/p2534413445.jpg)
### 开、高、低的价格，成交量
* period_df['open'] = df['open'].resample(rule=rule_type).first()
* period_df['high'] = df['high'].resample(rule=rule_type).max()
* period_df['low'] = df['low'].resample(rule=rule_type).min()
* period_df['volume'] = df['volume'].resample(rule=rule_type).sum()
* period_df = period_df[['open', 'high', 'low', 'close', 'volume']]

![](https://img3.doubanio.com/view/photo/l/public/p2534413432.jpg)
### 第二种方法：将1分钟数据转为5分钟数据
* rule_type = '5T'
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='left', closed='left').agg
* ({'open': 'first','high': 'max','low': 'min','close': 'last','volume': 'sum',})

![](https://img3.doubanio.com/view/photo/l/public/p2534538153.jpg)
* period_df = period_df[['open', 'high', 'low', 'close', 'volume']]
* base参数：帮助确定转换周期开始的时间
* label='left', closed='left'，建议统一设置成'left'

![](https://img1.doubanio.com/view/photo/l/public/p2534538159.jpg)
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=1, label='left', closed='left')
* base=1，使1分钟转换成5分钟的起点分钟时间推后1位，即base=0时，5分钟的起点为第0分钟开始（0-4分钟），base=1则为第1分钟开始（1-5分钟），以此类推。

![](https://img3.doubanio.com/view/photo/l/public/p2534538162.jpg)
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=2, label='left', closed='left')
* base=2，则为第1分钟开始（2-6分钟），因为有一些策略放弃前几分钟的数据，采用另类的及时方式来提高策略的有效性，可以采用参数穷举得到收益率差异。

![](https://img3.doubanio.com/view/photo/l/public/p2534538152.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538166.jpg)
### label='left'
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='left', closed='left')

![](https://img3.doubanio.com/view/photo/l/public/p2534538744.jpg)
### label='right'
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='right', closed='left')

![](https://img3.doubanio.com/view/photo/l/public/p2534538750.jpg)
### closed='right'
* period_df = df.resample(rule=rule_type, on='candle_begin_time', base=0, label='left', closed='right')

![](https://img3.doubanio.com/view/photo/l/public/p2534538743.jpg)
### 去除不必要的数据，去除一天都没有交易的周
* period_df.dropna(subset=['open'], inplace=True)
### 去除成交量为0的交易周期
* period_df = period_df[period_df['volume'] > 0]

![](https://img3.doubanio.com/view/photo/l/public/p2534538763.jpg)
### rule的取值
* S：secondly frequency，秒
* T：minutely frequency，分钟
* H：hourly frequency，小时
* D：calendar day frequency，日
* W：weekly frequency，周
* M：month end frequency，月
* Q：quarter end frequency，季
* A：year end frequency，年

![](https://img3.doubanio.com/view/photo/l/public/p2534538754.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534538758.jpg)
## 6.4 groupby分组
### 导入数据
* df = pd.read_csv('/Users/jxing/Desktop/coin_quant_class/data/class5/BITFINEX-1H-data-20180124.csv', skiprows=1)

![](https://img3.doubanio.com/view/photo/l/public/p2534538762.jpg)
### 根据'candle_begin_time'进行group，将相同'交易日期'的行放入一个group，
* print(df.groupby('candle_begin_time'))  # 生成一个group对象。不会做实质性操作，只是会判断是否可以根据该变量进行groupby。

![](https://img3.doubanio.com/view/photo/l/public/p2534542766.jpg)
### group后可以使用相关函数，size()计算每个group的行数
* print(df.groupby('candle_begin_time').size())  # 每小时交易的币的个数

![](https://img3.doubanio.com/view/photo/l/public/p2534542771.jpg)
### 根据'symbol'进行group，将相同'symbol'的行放入一个group
* print(df.groupby('symbol').size())  # 每个币交易的小时数

![](https://img3.doubanio.com/view/photo/l/public/p2534542776.jpg)
### 获取其中某一个group
* print(df.groupby('candle_begin_time').get_group('2018-01-24 00:00:00'))

![](https://img3.doubanio.com/view/photo/l/public/p2534542773.jpg)
* print(df.groupby('symbol').get_group('BTCUSD'))

![](https://img1.doubanio.com/view/photo/l/public/p2534542777.jpg)
### 其他常见函数
* print(df.groupby('symbol').describe())  # 只会对数值变量进行describe
* print(df.groupby('symbol').head(3))
* print(df.groupby('symbol').tail(3))  # 每个group里面的行顺序，会保留。
* print(df.groupby('symbol').first())
* print(df.groupby('symbol').last())
* print(df.groupby('symbol').nth(2))

![](https://img3.doubanio.com/view/photo/l/public/p2534542774.jpg)
### 将group变量设置为index
* print(df.groupby('symbol').nth(2))

![](https://img3.doubanio.com/view/photo/l/public/p2534542770.jpg)
### 将group变量【不】设置为index
* print(df.groupby('symbol', as_index=False).nth(2))

![](https://img1.doubanio.com/view/photo/l/public/p2534542767.jpg)
### 在group之后，取一部分变量进行计算
### 计算每个group的均值
* print(df.groupby('symbol')['close', 'volume'].mean())
### 计算每个group的最大值
* print(df.groupby('symbol')['close', 'volume'].max())

![](https://img3.doubanio.com/view/photo/l/public/p2534543146.jpg)
### 计算每个group的加总
* print(df.groupby('symbol')['volume'].sum())

![](https://img3.doubanio.com/view/photo/l/public/p2534543145.jpg)
### 计算该数据在每个group中的排名
* print(df.groupby('candle_begin_time')['volume'].rank())
* print(df.groupby('candle_begin_time')['volume'].rank(pct=True))

![](https://img1.doubanio.com/view/photo/l/public/p2534543157.jpg)

![](https://img3.doubanio.com/view/photo/l/public/p2534543153.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534543149.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534543150.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534543161.jpg)

> END
