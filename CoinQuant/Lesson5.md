# 第5课：Pandas入门操作
## 目录
* [5.1 数据导入](#51-数据导入)
* [5.2 查看、选取数据](#52-查看选取数据)
* [5.3 列操作](#53-列操作)
* [5.4 筛选、缺失处理](#54-筛选缺失处理)
* [5.5 合并、去重、时间](#55-合并去重时间)
* [5.6 字符串、滚动操作](#56-字符串滚动操作)

## 5.1 数据导入
### pd.read_csv
![](https://img3.doubanio.com/view/photo/l/public/p2533823204.jpg)
* skiprows = 3  # 该参数代表跳过数据文件的的第3行不读入。
* nrows = 15  # nrows，只读取前n行数据，若不指定，读入全部的数据。
* index_col = ['candle_begin_time']  # 将指定列设置为index。若不指定，index默认为0, 1, 2, 3, 4...
* error_bad_lines = False  # 当某行数据有问题时，报错。设定为False时即不报错，直接跳过该行。当数据比较脏乱的时候用这个。

![](https://img3.doubanio.com/view/photo/l/public/p2533823200.jpg)

## 5.2 查看、选取数据
### df.sample(n=3) 随机抽取3行
* df.shape  # 输出dataframe有多少行、多少列。
* df.shape[0]  # 取行数量，相应的列数量就是df.shape[1]。
* df.columns  # 顺序输出每一列的名字，演示如何for语句遍历。
* df.index  # 顺序输出每一行的名字，可以for语句遍历。
* df.dtypes  # 数据每一列的类型不一样，比如数字、字符串、日期等。该方法输出每一列变量类型。
* df.head(3)  # 看前3行的数据，默认是5。与自然语言很接近。
* df.tail(3)  # 看最后3行的数据，默认是5。

![](https://img3.doubanio.com/view/photo/l/public/p2533824004.jpg)
### df.sample(fac=0.5) 抽取固定比例，可以用frac参数
![](https://img3.doubanio.com/view/photo/l/public/p2533824010.jpg)
### pd.set_option('expand_frame_repr', False) 当列太多时不换行
![](https://img1.doubanio.com/view/photo/l/public/p2533824007.jpg)
### pd.set_option("display.max_rows", 1000) 设定显示最大的行数
![](https://img3.doubanio.com/view/photo/l/public/p2533824005.jpg)
### pd.set_option('precision', 8) 浮点数的精度
![](https://img1.doubanio.com/view/photo/l/public/p2533824008.jpg)

## 5.3 列操作
* loc操作：通过label（columns和index的名字）来读取数据。
* iloc操作：通过position来读取数据。
* [pandas基础操作](class5/pandas基础操作.py)

### 统计函数：求均值
* df[['close', 'volume']].mean(axis=0)  # 求每一列的均值，在行末新增一行显示统计结果。
* df[['close', 'volume']].mean(axis=1)  # 求n列每行的均值，在列末新增一列显示统计结果。
* axis=0或者1要搞清楚。axis=1，代表对整几列进行操作。axis=0（默认）代表对几行进行操作。实际中弄混很正常，到时候试一下就知道了。

![](https://img3.doubanio.com/view/photo/l/public/p2533824801.jpg)
### max、min、std、count、median、quantile
![](https://img3.doubanio.com/view/photo/l/public/p2533824826.jpg)
### shift、dift
* df['下周期close'] = df['close'].shift(-1)  # 读取上一行的数据，若参数设定为3，就是读取上三行的数据；若参数设定为-1，就是读取下一行的数据。
* del df['下周期close']  # 删除某一列的方法。
* df['涨跌'] = df['close'].diff(-1)  # 求本行数据和上一行数据相减得到的值。
* df.drop(['涨跌'], axis=1, inplace=True)  # 删除某一列的另外一种方式，inplace参数指是否替代原来的df。

![](https://img1.doubanio.com/view/photo/l/public/p2533824818.jpg)
### cum(cumulative)类函数
* df['涨跌幅'] = df['close'].pct_change(1)  # 类似于diff，但是求的是两个数直接的比例，相当于求涨跌幅。

![](https://img3.doubanio.com/view/photo/l/public/p2533824812.jpg)
* df['close_排名'] = df['close'].rank(ascending=True, pct=False)  # 输出排名。ascending参数代表是顺序还是逆序。

![](https://img1.doubanio.com/view/photo/l/public/p2533824819.jpg)
* df['close_排名'] = df['close'].rank(ascending=True, pct=True)  # pct参数代表输出的是排名还是排名比例。

![](https://img3.doubanio.com/view/photo/l/public/p2533824806.jpg)
* df['close'].value_counts()  # 计数。统计该列中每个元素出现的次数。返回的数据是Series。

![](https://img1.doubanio.com/view/photo/l/public/p2533824799.jpg)

## 5.4 筛选、缺失处理
### 筛选操作，根据指定的条件，筛选出相关的数据。
* df['symbol'] == 'AIDBTC'  # 判断交易对代码是否等于BTCUSD。
* df[df['symbol'] == 'BTCUSD']  # 将判断为True的输出：选取交易对代码等于BTCUSD的行。
* df[df['symbol'] == 'BTCUSD'].index  # 输出判断为True的行的index。
* df[df['symbol'].isin(['BTCUSD', 'LTCUSD', 'ETHUSD'])]  # 选取代码等于'BTCUSD'或'LTCUSD '或'ETHUSD'的行。

![](https://img3.doubanio.com/view/photo/l/public/p2533862015.jpg)

* df[df['close'] < 10.0])  # 选取收盘价小于10的行。
* df[(df['close'] < 10.0) & (df['symbol'] == 'AIDUSD')]  # 两个条件，或者的话就是|。

![](https://img3.doubanio.com/view/photo/l/public/p2533862005.jpg)
### 删除缺失值
![](https://img3.doubanio.com/view/photo/l/public/p2533862012.jpg)
* df.dropna(how='any')  # 将带有空值的行删除。how='any'意味着，该行中只要有一个空值，就会删除，可以改成all。
* df.dropna(subset=['12小时', 'close'], how='all')  # subset参数指定在特定的列中判断空值。
* all代表全部为空，才会删除该行；any只要一个为空，就删除该行。

![](https://img3.doubanio.com/view/photo/l/public/p2533862021.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533862029.jpg)
### 补全缺失值
* df.fillna(value=0)  # 直接将缺失值赋值为固定的值。
* df['12小时'].fillna(value=df['close'], inplace=True)  # 直接将缺失值赋值其他列的数据。

![](https://img1.doubanio.com/view/photo/l/public/p2533862017.jpg)
* df.fillna(method='ffill')  # 向上寻找最近的一个非空值，以该值来填充缺失的位置，全称forward fill，非常有用。

![](https://img3.doubanio.com/view/photo/l/public/p2533862025.jpg)
* df.fillna(method='bfill')  # 向下寻找最近的一个非空值，以该值来填充确实的位置，全称backward fill。

![](https://img3.doubanio.com/view/photo/l/public/p2533862004.jpg)
### 找出缺失值
* df.notnull()  # 判断是否为空值，反向函数为isnull()。
* df[df['12小时'].notnull()]  # 将'12小时'列为空的行输出。

![](https://img1.doubanio.com/view/photo/l/public/p2533862019.jpg)

## 5.5 合并、去重、时间
### 排序函数
* df.sort_values(by=['candle_begin_time'], ascending=0)  # by参数指定按照什么进行排序，acsending参数指定是顺序还是逆序，1顺序，0逆序。

![](https://img3.doubanio.com/view/photo/l/public/p2533947760.jpg)
* df.sort_values(by=['symbol', 'candle_begin_time'], ascending=[0, 0])  # 按照多列进行排序。

![](https://img1.doubanio.com/view/photo/l/public/p2533947757.jpg)
### 选取行列，合并两个DataFrame
* df1 = df.iloc[0:10][['candle_begin_time', 'symbol', 'close', 'volume']]
* df2 = df.iloc[5:15][['candle_begin_time', 'symbol', 'close', 'volume']]

![](https://img3.doubanio.com/view/photo/l/public/p2533947763.jpg)
* df1.append(df2)  # append操作，将df1和df2上下拼接起来。注意观察拼接之后的index。index可以重复。

![](https://img3.doubanio.com/view/photo/l/public/p2533947753.jpg)
* df3 = df1.append(df2, ignore_index=True)  # ignore_index参数，用户重新确定index。

![](https://img3.doubanio.com/view/photo/l/public/p2533947754.jpg)
### 对数据进行去重
* df3.drop_duplicates(subset=['candle_begin_time', 'symbol'], keep='first', inplace=True)
* subset参数用来指定根据哪类类数据来判断是否重复。若不指定，则用全部列的数据来判断是否重复。
* 在去除重复值的时候，我们是保留上面一行还是下面一行？first保留上面一行，last保留下面一行，False就是一行都不保留。

![](https://img3.doubanio.com/view/photo/l/public/p2533947756.jpg)
* df.reset_index(inplace=True)  # 重置index。

![](https://img1.doubanio.com/view/photo/l/public/p2533947768.jpg)
* df.reset_index(inplace=True, drop=True)  # 重置index，删除旧的索引列。

![](https://img3.doubanio.com/view/photo/l/public/p2533947765.jpg)
* df.rename(columns={'close': '收盘价', 'open': '开盘价'})  # rename函数给变量修改名字。使用dict将要修改的名字传给columns参数。

![](https://img1.doubanio.com/view/photo/l/public/p2533947767.jpg)
* df.empt  # 判断一个df是不是为空，此处输出不为空。

![](https://img1.doubanio.com/view/photo/l/public/p2533948628.jpg)
pd.DataFrame().empty  # pd.DataFrame()创建一个空的DataFrame，此处输出为空。

![](https://img3.doubanio.com/view/photo/l/public/p2533948626.jpg)
### 字符串处理
* df['symbol'].str[:3]

![](https://img1.doubanio.com/view/photo/l/public/p2533948629.jpg)
* df['symbol'].str.upper()  # 加上str之后可以使用常见的字符串函数对整列进行操作。
* df['symbol'].str.lower()
* df['symbol'].str.len()  # 计算字符串的长度,length。

![](https://img3.doubanio.com/view/photo/l/public/p2533948633.jpg)
df['symbol'].str.strip()  # strip操作，把字符串两边的空格去掉。

![](https://img1.doubanio.com/view/photo/l/public/p2533948627.jpg)
* df['symbol'].str.contains('AID')  # 判断字符串中是否包含某些特定字符。

![](https://img1.doubanio.com/view/photo/l/public/p2533948638.jpg)
* df['symbol'].str.replace('AID', 'AVT')  # 进行替换，将sz替换成sh。

![](https://img3.doubanio.com/view/photo/l/public/p2533948635.jpg)

## 5.6 字符串、滚动操作
![](https://img3.doubanio.com/view/photo/l/public/p2533948630.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533948632.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533949080.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533949075.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533949078.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533949069.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533949065.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533949059.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533949058.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533949076.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533949071.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533949098.jpg)

> END
