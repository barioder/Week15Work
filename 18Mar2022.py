import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# car_sales = { "Bmw":[20000,30000,40000,50000], "Lambo":[100000,200000,300000,400000], "Nissan":[9000,11000,17000,19000] }
#
# data = pd.DataFrame(car_sales)
#
# print(car_sales)
#
# print('----------------------------------------')
#
# car_sales = { "Bmw":[20000,30000,40000,50000], "Lambo":[100000,200000,300000,400000], "Nissan":[9000,11000,17000,19000] }
#
# print(data.columns[1:])
#
print('----------------------------')
# Create a dictionary that contains names and numbers of people.
# You need to create a DataFrame from the dictionary and add an index to it, which should be the name values.
# Then take a name from user input and output the row in the DataFrame, which corresponds to that row.

# data = {'name': ['Derrick', 'Steven', 'Andrew' ],
#         'numbers': [[780000000, 780100205], [780205150, 780012015], [791002500, 723547000]]}
#
# df = pd.DataFrame(data)
#
# print(df)
#
# df.set_index('name', inplace=True)
# print(df)
#
# input_name = input('What name do you want to find? ')
#
# print(f'Numbers under {input_name} ')
# print(df.loc[input_name])


print('------------------------------------')


# "Seats in a Theater." You are given an array that represents the occupancy of seats in a movie theater.
# A seat marked with 1 is occupied, while one marked 0 means the seat is free.
# However, the array is flat and 1-dimensional. Transform it into a 2-dimensional array, representing the rows of the seats.
# Each row in the theater has 5 seats and there are a total of 30 seats.
# Reshape the array into the corresponding shape and output the row at the given index, which is taken from user input.

seats_array = np.random.randint(0, 2, (1, 30))
# print(seats_array)

seats_array = seats_array.reshape(6, 5)

# print(seats_array)
# print('---------------------')

return_row = int(input('please enter the row number '))

while True:
        if return_row < 0 or return_row > 5:
                print('please enter a number from 0 to 5')
                return_row = int(input('please enter the row number '))
        else:
                print(seats_array[return_row])
                break


# Given a list of numbers and the number of rows (r), reshape the list into a 2-dimensional array.
# Note that r divides the length of the list evenly.
# First line: an integer (r) indicating the number of rows of the 2-dimensional arrayNext line: numbers separated by the space.
# An numpy 2d array of values rounded to the second decimal.


# Create housing prices, you need to calculate and output the number of houses that have a price that is above the average.
# To calculate the average price of the houses, you need to divide the sum of all prices by the number of houses.

housing_prices = [500, 250, 900, 705, 150, 280, 848, 450, 600, 900, 400]

list_length = len(housing_prices)

sum_of_prices = sum(housing_prices)

average_price = sum_of_prices/list_length
print(average_price)
above_average = []
for price in housing_prices:
        if price > average_price:
                above_average.append(price)

print(f'Number of houses above average is {len(above_average)}')


# Download any csv file and plot out the that data in 3 different graphs in 1 figure.

covid_data = pd.read_csv("E:/Education/aws/class/Week 17/WHO-COVID-19-global-table-data.csv")

covid_data.drop(['Name', 'WHO Region', 'Cases - newly reported in last 7 days',
                 'Cases - newly reported in last 7 days per 100000 population', 'Cases - newly reported in last 24 hours',
                 'Deaths - cumulative total', 'Deaths - cumulative total per 100000 population',
                 'Deaths - newly reported in last 7 days', 'Deaths - newly reported in last 7 days per 100000 population',
                 'Deaths - newly reported in last 24 hours'], axis=1)

fig, axes = plt.subplots(nrows=1, ncols=3)

covid_data.plot(ax=axes[0], marker='o')

covid_data.plot(kind='bar', ax=axes[1])

covid_data.plot.scatter(y='Cases - cumulative total', x='Cases - cumulative total per 100000 population', ax=axes[2])

plt.show()