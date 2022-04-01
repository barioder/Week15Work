import numpy as np

# speed = [20, 45, 100, 24, 80, 90, 47]
#
# s = np.median(speed)
#
# print('median value', s)
#
# sum = np.sum(speed)
#
# print(sum)
#
# mean = np.mean(speed)
#
# print(mean)
# print('----------------------------------------')
# speed2 = np.array([20, 45, 100, 24, 80, 90, 47])
#
# sum = speed2.sum()
#
# print('sum ', sum)
#
# mean = speed2.mean()
#
# print('mean ', mean)
# print('-----------------')
# # greater than a number in an array
#
# speed2 = np.array([20, 45, 100, 24, 80, 90, 45, 47])
#
# print((75 > speed2).sum())
#
# print((speed2 > 50).sum())
#
# print((speed2 == 45).sum())
# print('------------------------------------')
# # numpy linespace
#
# array5 = np.linspace(1, 10)
# array6 = np.arange(1, 10)
#
# print('linspace', array5)
#
# print('arange', array6)
#
# print('--------------------------------')
# array7 = np.linspace(1, 20, 3)
# array8 = np.arange(1, 20, 3)
#
#
# print('linspace with length', array7)
#
# print('arange with step', array8)


# 1.Create a 2-D array and slice out the second number in the second column.

array1 = np.array([[25, 46, 80], [27, 78, 80]])

print(array1)

secNum = array1[1, 1]

print('Second number in second column: ', secNum)

print('-------------------------------------------------------')
# 2. Create a list of numbers and find out the median value in that list using
# a function.

list1 = [25, 65, 90, 68, 15, 48, 10]


def myMedian(arg):
    median = np.median(arg)

    return f'The median of {list1} is {median}'


value = myMedian(list1)
print(value)


print('-------------------------------------------------------')
# 3. Create an array with 20 random numbers and find out how many numbers is
# greater than,less than, or equal to 55.

random_array1 = np.random.randint(1, 100, (4, 5))

print(random_array1)

print(f'Numbers greater than 55 are {(random_array1 > 55).sum()}')


print(f'Numbers less than 55 are {(random_array1 < 55).sum()}')

print(f'Numbers equal to 55 are {(random_array1 == 55).sum()}')