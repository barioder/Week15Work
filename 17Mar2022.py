import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf
import mplfinance as mpf




plt.style.use('dark_background')

# start = dt.datetime(2021,3,17)
# end = dt.datetime.now()
#
#
# data = yf.download("AAPL",start, end)
#
# #print(data)
#
# stock_data = pd.DataFrame(data)
#
#
#
# #print(stock_data)
#
# #print(stock_data.head(20))
# #print(stock_data.tail(20))
# print(stock_data['Open'])
# print(stock_data['Close'])
#
#
# print(stock_data[['Open','Close']].plot(kind='line'))
#
# plt.show()
#
# def riot():
#     stock = yf.download("RIOT",start="2022-01-17",end="2022-02-17")
#
#     return stock
# print(riot())
#
#
#
# mpf.plot(stock_data,type='candlestick',volume=True
# ,style='yahoo',title='APPL')
# mpf.show()


# 1. Download any data csv and find out the total average for 3 columns.

covid_data = pd.read_csv("E:/Education/aws/class/Week 17/WHO-COVID-19-global-table-data.csv")

df = pd.DataFrame(covid_data)
print(df['Cases - cumulative total per 100000 population'].mean())
print(df['Cases - newly reported in last 7 days'].mean())
print(df['Cases - newly reported in last 7 days per 100000 population'].mean())

print(df.groupby(['Cases - cumulative total per 100000 population', 'Cases - newly reported in last 7 days',
         'Cases - newly reported in last 7 days per 100000 population']).mean())

print('----------------------------------------------------------')
# 2. Inside your new csv you downloaded, remove 1 column out of your
# data frame.
print(df)

print('------------------------------------------------------------')
df.drop('Name', axis=1, inplace=True)
print(df)

# 3. Use a scatter plot with different colors to display your data.

df.plot.scatter(x= 'Cases - newly reported in last 7 days', y='Cases - cumulative total per 100000 population')

plt.show()



