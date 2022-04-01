import numpy as np

# 1. What method you use to add brackets to an array?
# Answer = ndmin

arra_1 = np.array([1, 2, 3, 4], ndmin=5)

print(arra_1)

print('--------------------------------------------------')
# 2. What's the output of this code?x = np.arange(1,5,2)
# Answer = [1 3]
x = np.arange(1,5,2)
print(x.ndim)
print(x)

print('--------------------------------------------------')

# 3. Fill in the blank. Import numpy as _____.
# Answer = np


print('--------------------------------------------------')

# 4. Create an array that outputs 6 rows and 6 columns. Then reshape it but it has to be more than 2 rows.

array_2 = [[1, 2, 3, 4, 5, 6], [2, 5, 6, 8, 7, 1], [2, 8, 1, 9, 5, 8], [8, 9, 2, 5, 6, 7],
           [5, 6, 8, 9, 9, 7], [8, 5, 9, 3, 6, 7]]
array_2 = np.array(array_2)

array_reshape = array_2.reshape(4, 9)

print(array_reshape)

print('--------------------------------------------------')

# 5. Create a 2 d array with 6 columns and grab the 2 numbers in the second column.

array_5 = [[1, 2, 3, 4, 5, 6], [2, 5, 6, 8, 7, 1], [2, 8, 1, 9, 5, 8]]

array5 = np.array(array_5)
print(array5)

value = array5[1, 1]
value2 = array5[1][:2]

print('--------------',value2)

print(value)

print('--------------------------------------------------')

# 6. True or False? I could add boolean values in an array method?

#  answer = True


# 7. What is the out put of this code? y = np.([1,2,3,4]) print(y)

#  answer = syntax error

# 8. What's the output of this code? x = np.array([2,4,5,6]) y = np.array([12,14,16,18]) print(np.add(x,y))
# answer = [14 18 21 24]
x = np.array([2,4,5,6])
y = np.array([12,14,16,18])

print(y.size)

print(np.add(x,y))
print('--------------------------------------------------------------------')

# 9. How do you find out the size of an array?

# answer = print(np.size)

# 10. Whats the output of this code? x = np.linspace(1,5) print x

#  answer = [1. 5.]
x = np.linspace(1,5)

print (x)

print('----------------------------------------------------------------------')
# 11. Create an array with 25 random numbers from 20 to 100. Find out how many numbers is greater than 55.

array_random = np.random.randint(20, 100, (5, 5))

result = (array_random > 55).sum()

print(result)

print('----------------------------------------------------------------------')
# 12. Create a list called mph, the length of that list have to be 12.
# Using a function, find out the average mph in that list and also find the median value.

mph = [120, 145, 50, 90, 20, 180, 100, 210, 150, 70, 190, 95]

def speed(arg):
    average_mph = np.average(mph)

    median_mph = np.median(mph)

    print('Average mph ', average_mph, '\n', 'Median mph ', median_mph)

speed(mph)