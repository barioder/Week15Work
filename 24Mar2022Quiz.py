import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
# 1. Create a list called basketball players.
# You need to calculate and output how many players are in the range of one standard deviation from the mean.



# 2. You are given a task to find all of the whole numbers below 100 that are multiples of borh 3 and 5.
# Create an array of numbers below 100 that are multiples of both 3 and 5, and out put it.

list = []
x = 0

while x < 100:
    if x % 3 == 0 and x % 5 == 0:
        list.append(x)

    x += 1

array1 = np.array(list)
print(array1)

print('---------------------------------------')
# 3 Create a 2 -D Array and slice out 3 numbers out the second column.

array3 = np.array([[4, 5, 6, 8], [7, 10, 15, 20], [12, 14, 16, 18], [22, 63, 85, 86]])
print(array3)
print(array3[0:3, 1])

# 4 Wallstreet wants to know the open and close price for amazon.
# Download the amazon csv or yfinance and print out only the open and close price for the amazon stock.

result = pd.read_csv("E:/WORK/VETTING/2021/AUGUST/VETTING 44/TRAVEL LISTS/muqeem/SPY.csv")

print(result[['Open', 'Close']])


# 5 Download and csv file and put it in your dataframe. Your task is to rename a column inside your dataframe.

df = pd.read_csv("E:/WORK/VETTING/2021/AUGUST/VETTING 44/TRAVEL LISTS/muqeem/SPY.csv")

df.rename(columns={'Open':'OPEN'}, inplace=True)

print(df)

# 6 Create "2" 1-D array and divide both of the array's

array1 = np.array([[1, 2, 3], [5, 6, 7]])
array2 = np.array([[2, 3, 4], [5, 1, 5]])

print(array1 / array2)

# Create a scatter plot that print out stars instead of circles inside your graph.

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([100, 200, 300, 400, 500, 600])

plt.scatter(x, y, color='r', marker='*')

plt.xlabel('X')
plt.ylabel('Y')

plt.show()

