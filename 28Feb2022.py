import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('dark_background')
#
# arr = [15, 25, 67, 60, 45, 67, 25, 99, 81, 27]
#
# arr2 = np.arange(0, 10, 1)
#
# def sort_algo():
#     n = len(arr)
#
#     for i in range(n):
#             for j in range(n-i-1):
#                 plt.bar(arr2, arr)
#                 plt.pause(0.01)
#                 plt.clf()
#
#                 if arr[j] > arr[j+1]:
#                     arr[j+1], arr[j] = arr[j], arr[j+1]
#
#
# sort_algo()
#
# plt.show()


# 1. Create a 6-D array and flatten it to 1-D array.

array1 = np.array([[[[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]]])

print('array1 ', array1.ndim)


array2 = array1.flatten()
print(array2)

print('array2 ', array2.ndim)

print('--------------------------------------------------')
# 2. Create a whileloop that prints only even numbers in a range of 20
# but skips 16.

for i in range(1, 20):
    if i % 2 == 0:
        if i != 16:
            print(i)
print('---------------------------------------------------')
# 3. Steph Curry has scored [22,55,43,31,38] points in 5 games. Using a
# function, find out his total points average in 5 games.


def ave(scores):
    length = len(scores)

    total_score = sum(scores)
    average = total_score/length
    return average


curry_scores = [22, 55, 43, 31, 38]

print(ave(curry_scores))

print('---------------------------------------------')
# 4. Create a list and convert it into a tuple.

list = ['Dog', 'Cat', 'Parrot']

tuple1 = tuple(list)

print(tuple1)


# 5.Create any sorting algorithm using matplotlib.(Use my resources if needed)
plt.style.use('dark_background')

arr1 = [61, 20, 15, 50, 10, 19, 30, 1]

arr2 = np.arange(0, 8, 1)

def selectSort(arg):
    for i in range(len(arg)):
        midindex = i
