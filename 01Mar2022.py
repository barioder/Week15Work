import numpy as np

# 1.50 percent of the class failed the exam,
# create a list of student scores that scored under a 70.

scores = [85, 50, 75, 65, 80, 90, 60, 45]

result = np.percentile(scores, 30)

print(result)
print('----------------------------------------------------------')
# 2.Create a 6-D array and transform it to all rows.

array1 = np.array([[[[[[1, 12, 16], [2, 6, 11], [3, 18, 15]]]]]])
print(f'Num of dimension for array1: {array1.ndim}')


print(np.vstack((array1)))
print(array1)
array1 = array1.reshape(9, 1)
print(array1)


print(array1.flatten())

print('-------------------------------------------------------------')
# 3.Create a 8-D array and reshape the array.

array8 = np.array([[[[[[[[2, 6, 8], [10, 12, 14], [16, 18, 20], [22, 24, 26]]]]]]]])

print(f'Num of dimensions for array8: {array8.ndim}')

array8 = array8.reshape(6, 2)
print(array8)

print('-------------------------------------------------------------')
# 4.Create a x array and y array and multiple it than reshape the new array.

x = np.array([[2, 5, 6], [8, 10, 11]])
y = np.array([[6, 2, 3], [2, 5, 8]])

z = x * y
print(z)

print('Reshape')
z_reshape = z.reshape(3, 2)
print(z_reshape)