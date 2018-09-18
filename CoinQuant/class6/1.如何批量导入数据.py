import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# =====导入EOSUSD每一天的1分钟数据
df = pd.read_csv('/Users/jxing/Desktop/coin_quant_class/data/class6/BITFINEX/EOSUSD/BITFINEX_EOSUSD_20170701_1T.csv',
                 skiprows=1,
                 parse_dates=['candle_begin_time'])

# =====批量导入EOSUSD所有天的一分钟数据
# 系统自带函数os.walk，用于遍历文件夹中的所有文件，os是python自带的系统库
# 演示os.walk
for root, dirs, files in os.walk('/Users/jxing/Desktop/coin_quant_class/data'):
    # root输出文件夹，dirs输出root下所有的文件夹，files输出root下的所有的文件
    print('root:', root)
    print('dirs:', dirs)
    print('files:', files)
    print()

# 批量读取文件名称
file_list = []
for root, dirs, files in os.walk('/Users/jxing/Desktop/coin_quant_class/data/class6'):
    # 当files不为空的时候
    if files:
        for f in files:
            if f.endswith('.csv'):
                file_list.append(f)

# 遍历文件名，批量导入数据
all_data = pd.DataFrame()
for file in sorted(file_list):
    print(file)
    # 导入数据
    df = pd.read_csv('/Users/jxing/Desktop/coin_quant_class/data/class6/BITFINEX/EOSUSD/' + file,
                     skiprows=1,
                     parse_dates=['candle_begin_time'])
    #  合并数据
    all_data = all_data.append(df, ignore_index=True)  # 注意此时若一下子导入很多文件，可能会内存溢出

# 对数据进行排序
all_data.sort_values(by=['candle_begin_time'], inplace=True)

# 将数据存入hdf文件中
all_data.to_hdf(
    '/Users/jxing/Desktop/coin_quant_class/data/class6/eos_1min_data.h5',
    key='all_data',
    mode='w')

# 从hdf中读取文件
all_data = pd.read_hdf('/Users/jxing/Desktop/coin_quant_class/data/class6/eos_1min_data.h5', key='all_data')
print(all_data)
