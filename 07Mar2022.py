import numpy as np

import matplotlib.pyplot as plt

# 1.Create a 2-D array and grab 3 numbers in the second column.

arry2 = np.array([[2, 5, 9, 12], [8, 1, 16, 18], [20, 23, 26, 28], [30, 31, 36, 39]])

print(arry2)
print(arry2[:3, 1])

print('---------------------------------------------------------------')
# 2.Create a list called company_data, using a funtion the company needs
# to know the total average,the variance,and how spread out the data is.

company_data = [25, 65, 45, 15, 88, 60, 36]

def comp(arg):
    # arry1 = np.array(arg)

    average = f'The Average is {np.mean(arg)}'
    variance = f'The Variance is {np.var(arg)}'
    stdev = f'The stdev {np.std(arg)}'

    return average, variance, stdev

data = comp(company_data)

print(data[0])
print(data[1])
print(data[2])


print('---------------------------------------------------------------')

# 3.Create 2 arrays showing the x axis from 20 to 100 and the y axis from 120
# to 200 (use matplotlib to visualize the array for x and y).

x_axis = np.array([20, 60, 80, 100])
y_axis = np.array([120, 160, 180, 200])

plt.plot(x_axis, y_axis)
plt.show()

# 4.Create a 2-d array and multiple both columns then reshape the new array.

array3 = np.array([[1, 2, 3, 4], [5, 6, 8, 10]])
arry4 = np.array([[5, 3, 6, 7], [1, 2, 5, 6]])

arry5 = array3 * arry4

print(arry5)

print(arry5.reshape(4, 2))
# 5.Create any  sorting algorithm and show us the animation using matplotlib.
