import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


statement = {'Balance': [3500, 4500, 7000, 250, 500, 1500],
             'Deposit': [1500, 7500, 8000, 8500, 25600, 1500],
             'Withdraw': [6500, 7200, 78000, 3100, 4700, 1000]}

BankStatement = pd.DataFrame(statement)

fig, axes = plt.subplots(nrows=1, ncols=2)
BankStatement.plot(ax=axes[0], marker='o')

BankStatement.plot(kind='bar', ax=axes[1])

plt.show()


# 1. Download the covid csv file and find out the shape
# and the number of dimension of that file.

covid_data = pd.read_csv("E:/Education/aws/class/Week 17/WHO-COVID-19-global-table-data.csv")

print(covid_data)
print(covid_data.shape)

print(covid_data.ndim)

print('------------------------------------------------------')
# 2. The previous covid csv you downloaded, print the output
# for the amount of new cases for each month.

# print(covid_data['248897'])

print(covid_data['Cases - newly reported in last 7 days'])

# 3. Plot that data in a pie graph showing the Percentages.
# 4. Find the percentile for all the new cases.
























