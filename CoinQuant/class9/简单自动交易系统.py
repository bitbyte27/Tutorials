from datetime import datetime, timedelta
import pandas as pd
from time import sleep
import ccxt
from program.class9.Trade import next_run_time, place_order, get_okex_candle_data, auto_send_email
from program.class8.Signals import signal_moving_average
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


"""
自动交易主要流程
 
# 通过while语句，不断的循环

# 每次循环中需要做的操作步骤
    1. 更新账户信息
    2. 获取实时数据
    3. 根据最新数据计算买卖信号 
    4. 根据目前仓位、买卖信息，结束本次循环，或者进行交易
    5. 交易
"""

# =====参数
time_interval = '15m'  # 间隔运行时间，不能低于5min

exchange = ccxt.okex()  # 创建交易所，此处为okex交易所
exchange.apiKey = 'your_api_key'  # 此处加上自己的apikey和secret，都需要开通交易权限
exchange.secret = 'your_api_secret'

symbol = 'OKB/USDT'  # 交易品种
base_coin = symbol.split('/')[-1]
trade_coin = symbol.split('/')[0]

para = [20, 200]  # 策略参数


# =====主程序
while True:
    # ===监控邮件内容
    email_title = '策略报表'
    email_content = ''

    # ===从服务器更新账户balance信息
    balance = exchange.fetch_balance()['total']
    base_coin_amount = float(balance[base_coin])
    trade_coin_amount = float(balance[trade_coin])
    print('当前资产:\n', base_coin, base_coin_amount, trade_coin, trade_coin_amount)

    # # ===sleep直到运行时间
    run_time = next_run_time(time_interval)
    sleep(max(0, (run_time - datetime.now()).seconds))
    while True:  # 在靠近目标时间时
        if datetime.now() < run_time:
            continue
        else:
            break

    # ===获取最新数据
    while True:
        # 获取数据
        df = get_okex_candle_data(exchange, symbol, time_interval)
        # 判断是否包含最新的数据
        _temp = df[df['candle_begin_time_GMT8'] == (run_time - timedelta(minutes=int(time_interval.strip('m'))))]
        if _temp.empty:
            print('获取数据不包含最新的数据，重新获取')
            continue
        else:
            break

    # ===产生交易信号
    df = df[df['candle_begin_time_GMT8'] < pd.to_datetime(run_time)]  # 去除target_time周期的数据
    df = signal_moving_average(df, para=para)
    signal = df.iloc[-1]['signal']
    print('\n交易信号', signal)

    # =====卖出品种
    if trade_coin_amount > 0 and signal == 0:
        print('\n卖出')
        # 获取最新的卖出价格
        price = exchange.fetch_ticker(symbol)['bid']  # 获取买一价格
        # 下单
        place_order(exchange, order_type='limit', buy_or_sell='sell', symbol=symbol, price=price*0.98, amount=trade_coin_amount)
        # 邮件标题
        email_title += '_卖出_' + trade_coin
        # 邮件内容
        email_content += '卖出信息：\n'
        email_content += '卖出数量：' + str(trade_coin_amount) + '\n'
        email_content += '卖出价格：' + str(price) + '\n'

    # =====买入品种
    if trade_coin_amount == 0 and signal == 1:
        print('\n买入')
        # 获取最新的买入价格
        price = exchange.fetch_ticker(symbol)['ask']  # 获取卖一价格
        # 计算买入数量
        buy_amount = base_coin_amount / price
        # 获取最新的卖出价格
        place_order(exchange, order_type='limit', buy_or_sell='buy', symbol=symbol, price=price*1.02, amount=buy_amount)
        # 邮件标题
        email_title += '_买入_' + trade_coin
        # 邮件内容
        email_content += '买入信息：\n'
        email_content += '买入数量：' + str(buy_amount) + '\n'
        email_content += '买入价格：' + str(price) + '\n'

    # =====发送邮件
    # 每个半小时发送邮件
    if run_time.minute % 30 == 0:
        # 发送邮件
        auto_send_email('your_email_address', email_title, email_content)

    # =====本次交易结束
    print(email_title)
    print(email_content)
    print('=====本次运行完毕\n')
    sleep(6 * 1)
