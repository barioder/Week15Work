import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
# 1.Create in pandas the name of the rows is the car and the sales will be the values.

sales = {'Jeep': [50, 20, 30, 40, 50],
         'BMW': [55, 60, 20, 25, 30]
         }

result = pd.DataFrame(sales)

print(result)

print('------------------------------------')
# 2.Create a pandas series with 1-D array.
array1 = np.array([25, 50, 60, 45, 70])

result_1 = pd.Series(array1)

print(result_1)

print('-----------------------------------------')
# 3.After you create the rows for cars and values for sales add the dates.

date_data = pd.date_range('20220314', periods=5)
sales_1 = pd.DataFrame(sales, index=date_data)

print(sales_1)

# shape of the data frame

print(sales_1.shape)

# transpose turns columns to rows
print(sales_1.transpose())


sales_1 = pd.DataFrame(sales)

print(sales_1.columns[1:])

print(sales_1['Jeep'])


print(sales_1.describe())

print('#########################')

print(sales_1.iloc[1])
print('......................')
print(sales_1.iloc[2])

print('...................')

print(sales_1.iloc[0:])

print('...................')

print(sales_1.loc[0::2])

print('*******************************')

print(sales_1.head(n=2))

print(sales_1.tail(n=2))

df = pd.read_csv("E:/WORK/VETTING/2021/AUGUST/VETTING 44/TRAVEL LISTS/muqeem/data_table_for_daily_case_trends__the_united_states.csv", skiprows=2)

print(df)

print(df.info)

df.plot(kind='bar')
plt.title('New cases')
plt.show()