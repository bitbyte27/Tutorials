## Moving Averages - Simple and Exponential
[Moving Averages - Simple and Exponential](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_averages#simple_vs_exponential_moving_averages)

## Introduction
* Moving averages smooth the price data to form a trend following indicator. They do not predict price direction, but rather define the current direction with a lag. Moving averages lag because they are based on past prices. Despite this lag, moving averages help smooth price action and filter out the noise. They also form the building blocks for many other technical indicators and overlays, such as Bollinger Bands, MACD and the McClellan Oscillator. The two most popular types of moving averages are the Simple Moving Average (SMA) and the Exponential Moving Average (EMA). These moving averages can be used to identify the direction of the trend or define potential support and resistance levels.

* 移动平均线可以平滑价格数据，形成趋势跟踪指标。他们并不预测价格方向，而是用滞后的方式来定义当前的方向。移动平均线之所以滞后，因为它们是基于过去的价格。尽管有这种滞后，移动平均线仍然有助于平稳价格移动和滤除噪音。它们也的构成了许多其他技术指标和覆盖的基石，如Bollinger波段、MACD和McClellan振荡器。最流行的两种移动平均法是简单移动平均法(SMA)和指数移动平均法(EMA)。这些移动平均线可以用来确定趋势的方向或确定潜在的支撑和阻力水平。

#### Here's a chart with both an SMA and an EMA on it:

![](pic/mova-1-intcexam.png)

## Simple Moving Average Calculation
* A simple moving average is formed by computing the average price of a security over a specific number of periods. Most moving averages are based on closing prices. A 5-day simple moving average is the five-day sum of closing prices divided by five. As its name implies, a moving average is an average that moves. Old data is dropped as new data comes available. This causes the average to move along the time scale. Below is an example of a 5-day moving average evolving over three days.
* 简单移动平均(SMA)是通过计算证券在特定时期内的平均价格而形成的。大多数移动均线都是基于收盘价。5天简单移动平均线是5天收盘价总和除以5。顾名思义，移动平均线就是移动的平均线。当新数据可用时，将删除旧数据。这导致平均沿时间尺度移动。下面是一个五天移动平均演变在三天内的例子。
* Daily Closing Prices: 11,12,13,14,15,16,17
* First day of 5-day SMA: (11 + 12 + 13 + 14 + 15) / 5 = 13
* Second day of 5-day SMA: (12 + 13 + 14 + 15 + 16) / 5 = 14
* Third day of 5-day SMA: (13 + 14 + 15 + 16 + 17) / 5 = 15
