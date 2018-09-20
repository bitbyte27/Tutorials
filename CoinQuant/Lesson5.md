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
* skiprows = 3  # 该参数代表跳过数据文件的的第3行不读入
* nrows = 15  # nrows，只读取前n行数据，若不指定，读入全部的数据
* index_col = ['candle_begin_time']  # 将指定列设置为index。若不指定，index默认为0, 1, 2, 3, 4...
* error_bad_lines = False  # 当某行数据有问题时，报错。设定为False时即不报错，直接跳过该行。当数据比较脏乱的时候用这个。

![](https://img3.doubanio.com/view/photo/l/public/p2533823200.jpg)

## 5.2 查看、选取数据
### df.sample(n=3) 随机抽取3行
* df.shape  # 输出dataframe有多少行、多少列。
* df.shape[0]  # 取行数量，相应的列数量就是df.shape[1]
* df.columns  # 顺序输出每一列的名字，演示如何for语句遍历。
* df.index  # 顺序输出每一行的名字，可以for语句遍历。
* df.dtypes  # 数据每一列的类型不一样，比如数字、字符串、日期等。该方法输出每一列变量类型
* df.head(3)  # 看前3行的数据，默认是5。与自然语言很接近
* df.tail(3)  # 看最后3行的数据，默认是5。
* df.sample(n=3)  # 随机抽取3行，想要去固定比例的话，可以用frac参数

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
![](https://img3.doubanio.com/view/photo/l/public/p2533824801.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533824826.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533824818.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533824812.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533824819.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533824806.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533824799.jpg)

## 5.4 筛选、缺失处理
![](https://img3.doubanio.com/view/photo/l/public/p2533862015.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533862005.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533862012.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533862021.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533862029.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533862017.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533862025.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533862004.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533862019.jpg)

## 5.5 合并、去重、时间
![](https://img3.doubanio.com/view/photo/l/public/p2533947760.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533947757.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533947763.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533947753.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533947754.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533947756.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533947768.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533947765.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533947767.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533948628.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533948626.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533948629.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533948633.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533948627.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2533948638.jpg)
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
