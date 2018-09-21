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
![](https://img3.doubanio.com/view/photo/l/public/p2533961196.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533961191.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533961184.jpg)
### 遍历文件名，批量导入数据
![](https://img3.doubanio.com/view/photo/l/public/p2533961185.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2533961174.jpg)
* all_data = all_data.append(df, ignore_index=True)  # 注意此时若一下子导入很多文件，可能会内存溢出。

![](https://img1.doubanio.com/view/photo/l/public/p2533961198.jpg)
### 对数据进行排序
* all_data.sort_values(by=['candle_begin_time'], inplace=True)

![](https://img3.doubanio.com/view/photo/l/public/p2533961210.jpg)
### 将数据存入csv文件中
![](https://img3.doubanio.com/view/photo/l/public/p2533961211.jpg)

## 6.2 HDF存取数据
![](https://img1.doubanio.com/view/photo/l/public/p2534180347.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534180332.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534180335.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534178845.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534179421.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534178881.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534179411.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534178851.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534178883.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534178858.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534178858.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534178979.jpg)

## 6.3 转变K线数据周期
![](https://img1.doubanio.com/view/photo/l/public/p2534413438.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534413442.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534413435.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534413433.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534413445.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534413432.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538153.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534538159.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538162.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538152.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538166.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538744.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538750.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538743.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538763.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534538754.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534538758.jpg)
## 6.4 groupby分组
![](https://img3.doubanio.com/view/photo/l/public/p2534538762.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542766.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542771.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542776.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542773.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534542777.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542774.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534542770.jpg)
![](https://img1.doubanio.com/view/photo/l/public/p2534542767.jpg)
![](https://img3.doubanio.com/view/photo/l/public/p2534543146.webp)
![](https://img3.doubanio.com/view/photo/l/public/p2534543145.webp)
![](https://img1.doubanio.com/view/photo/l/public/p2534543157.webp)
![](https://img3.doubanio.com/view/photo/l/public/p2534543153.webp)
![](https://img1.doubanio.com/view/photo/l/public/p2534543149.webp)
![](https://img3.doubanio.com/view/photo/l/public/p2534543150.webp)
![](https://img3.doubanio.com/view/photo/l/public/p2534543161.webp)

> END
