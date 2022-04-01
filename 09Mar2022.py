names = ['Derrick', 'Alex', 'Steven']
points = [45, 60, 90]

result = zip(names, points)


print(list(result))


# Homework assignment
# 1.Create a grid graph called Vaccine Data, and display
# in the graph of the data increasing then decreasing at the end.


import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 20, 30, 40, 50])
y = np.array([20, 25, 50, 30, 10])

plt.title('Vaccine Data')
plt.xlabel('Days')
plt.ylabel('Vaccinated Numbers')

plt.plot(x, y)

plt.grid()
plt.show()

# 2.Create a 4-D array and change it to a 1-D array.

array_4 = np.array([[[[1, 2, 3, 4], [5, 6, 7, 8]]]])
print(array_4)

print(f'Number of dimensions {array_4.ndim}')
array_4 = array_4.flatten()

print(array_4)

print('--------------------------------------------------------')
# 3.Create 4 different Graphs in 1 figure.
#  figure 1
x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([100, 200, 300, 400, 500, 600])

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Plot Graph')

# figure 2
x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([100, 200, 300, 400, 500, 600])

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title('Bar Graph')

# figure 3

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([100, 200, 300, 400, 500, 600])

plt.subplot(2, 2, 3)

plt.scatter(x, y, color='r')

plt.xlabel('X')
plt.ylabel('Y')

plt.title('Scatter Plot')

# figure 3
x = np.array([10, 20, 20, 5, 50, 60, 45, 90])

plt.subplot(2, 2, 4)
plt.plot(x, marker='*')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Marker')

plt.suptitle('Question 3')
plt.show()



print('----------------------------------------------------')
# 4.Find out the standard Deviation for the Vaccine Data.
x = np.array([10, 20, 30, 40, 50])
stddev = np.std(x)

print(f'The standard Deviation for the vaccine data is {stddev}')