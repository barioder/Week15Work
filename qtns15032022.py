import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.Create a table called "BankStatement" the rows are the Balance,Deposit,and withdraw.
# The columns is the amount in the dataframe. Print only the Deposit amount.

statement = {'Balance': [3500, 4500, 7000, 250, 500, 1500],
             'Deposit': [1500, 7500, 8000, 8500, 25600, 1500],
             'Withdraw': [6500, 7200, 78000, 3100, 4700, 1000]}

BankStatement = pd.DataFrame(statement)
# print(BankStatement)

print(BankStatement['Deposit'])

print('---------------------------------------------------------')

# 2. The "BankStatement" dataframe you created, we need to see it in 2 different graphs(subplot).

plt.subplot(1, 2, 1)
BankStatement.plot(kind='hist')
plt.title('Bar Graph')

plt.subplot(1, 2, 2)
BankStatement.plot(kind='bar')
plt.title('Histo')

plt.show()

print('---------------------------------------------------------')

# 3. Go to any website and download the csv file of that data. Then find out the mean, and
# standard deviation of that data.

players = pd.read_csv("E:/WORK/VETTING/2021/AUGUST/VETTING 44/TRAVEL LISTS/muqeem/england-premier-league-players-2018-to-2019-stats.csv", skiprows=2)

print(players)

print('######################################')
print(players.describe())
# 4. The new csv file you download, we need to see the data in any graph of 1 paticular row.

result = players['545529600']

result.plot(kind='bar')
plt.title('Result')
plt.show()