import pandas as pd
from program.class8.Functions import transfer_to_period_data
from program.class8.Signals import signal_bolling
from program.class8.Evaluate import equity_curve_with_long_and_short
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)


# # 导入数据
# df = pd.read_hdf('/Users/jxing/Desktop/coin_quant_class/data/class8/eth_1min_data.h5', key='all_data')
#
# # 转换数据周期
# rule_type = '15T'
# df = transfer_to_period_data(df, rule_type)
#
# # 计算交易信号
# para = [150, 3]
# df = signal_bolling(df, para)
#
# df = df[df['candle_begin_time'] >= pd.to_datetime('2017-01-01')]
# df.reset_index(inplace=True, drop=True)
#
# # 计算资金曲线
# df = equity_curve_with_long_and_short(df, leverage_rate=3, c_rate=2.0/1000)
#
# print('策略最终收益：', df.iloc[-1]['equity_curve'])
# exit()

# =====寻找最优参数
# 导入数据
all_data = pd.read_hdf('/Users/jxing/Desktop/coin_quant_class/data/class8/eth_1min_data.h5', key='all_data')
# 转换数据周期
rule_type = '15T'
all_data = transfer_to_period_data(all_data, rule_type)
# 选取时间段
all_data = all_data[all_data['candle_begin_time'] >= pd.to_datetime('2017-01-01')]
all_data.reset_index(inplace=True, drop=True)

# 构建参数候选组合
n_list = range(50, 500, 50)
m_list = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# 遍历所有参数组合
rtn = pd.DataFrame()
for m in m_list:
    for n in n_list:
        para = [n, m]

        # 计算交易信号
        df = signal_bolling(all_data.copy(), para)

        # 计算资金曲线
        df = equity_curve_with_long_and_short(df, leverage_rate=3, c_rate=2.0 / 1000)
        print(para, '策略最终收益：', df.iloc[-1]['equity_curve'])

        # 存储数据
        rtn.loc[str(para), '收益'] = df.iloc[-1]['equity_curve']

print(rtn.sort_values(by='收益', ascending=False))
