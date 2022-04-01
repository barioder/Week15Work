import matplotlib.pyplot as plt
import numpy as np

# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([8,7,6,5,4,3,2,1])
#
# plt.subplot(2,3,1)
# plt.plot(x,color = 'red',marker='o')
# plt.plot(y,color = 'yellow',marker='o')
#
#
#
#
# x = np.arange(1,10,1)
# y = np.arange(10,100,10)
#
font1 = {
   'family':'serif',
   'size':20
}
#
#
# plt.subplot(2,3,2)
# plt.plot(x,y)
# plt.xlabel('This is the label for X axis',color='red',fontdict=font1)
# plt.ylabel('This is the label for y axis',color='blue',fontdict=font1)
# plt.grid()
#
# y = np.array([100,93,85,75])
#
# students = ["George","Clara","Shawn","Shania"]
# c2 = ["blue","pink","green","red"]
#
#
# plt.subplot(2,3,3)
# plt.pie(y,labels=students,colors=c2,autopct='%1.1f%%')
#
#
# print(np.mean(y))
#
# x = np.random.randint(100,size=(100))
# y = np.random.randint(100,size=(100))
# colors = np.random.randint(100,size=(100))
# sizes = 15 * np.random.randint(100,size=(100))
#
# plt.subplot(2,3,4)
# plt.scatter(x,y,c=colors,s=sizes,cmap='jet',alpha=0.5,marker='*')
# plt.title('Scatter Stars Graph',fontdict=font1,color='red')
# plt.colorbar()
#
#
# plt.suptitle('4 Figures')
# plt.show()


# Roc nation record label has 4 artist that had their album come out last friday.
# In the first week,Rihanna sold 100,000,Kanye sold 95,000,J.cole sold 70,000,
# and Wale sold 35,000 in the first week. Display each sales in the first week using any graph in Matplotlib.

sales = [100000, 95000, 70000, 35000]
names = ['Rihanna', 'Kanye', 'J.cole', 'Wale']
#
# plt.bar(names, sales)
# plt.xlabel('Names')
# plt.ylabel('Sales')
# plt.show()

# Roc nation record label wants to also analyze the album sales
# for those 4 artist in 6 different graphs in 1 figure.

#  figure 1
y = np.array([100000, 95000, 70000, 35000])
x = np.array(['Rihanna', 'Kanye', 'J.cole', 'Wale'])

plt.subplot(3, 2, 1)
plt.plot(x, y)

# figure 2
plt.subplot(3, 2, 2)
plt.bar(x, y)

# figure 3
plt.subplot(3, 2, 3)

plt.scatter(x, y, color='r')

plt.xlabel('X')
plt.ylabel('Y')


# figure 4

plt.subplot(3, 2, 4)
plt.plot(x, y, marker='*')
plt.xlabel('X')
plt.ylabel('Y')

# figure 5
plt.subplot(3, 2, 5)
colors = np.random.randint(100,size=(4))
plt.scatter(x,y,c=colors,s=25,cmap='jet',alpha=0.5,marker='o')
plt.colorbar()

# figure 6
plt.subplot(3, 2, 6)
plt.plot(x, y)
plt.grid()
plt.show()



# Create a 2-D array and print only 1 column in that 2-D array.

array1 = np.array([[2, 5, 6, 8], [15, 25, 9, 12]])
print(array1)

row1 = array1[:, 1]
print(row1)

# Create a plot graph that have the x axis going up then down and then up,
# and the y axis going down up and down. (Use different colors for the lines for axis x and y.

x = np.array([5, 10, 40, 25, 20, 30, 50, 90])
y = np.array([10, 5, 1, 50, 80, 90, 40, 30])

plt.plot(x, color='Green')
plt.plot(y, color='brown')

plt.show()

# Create a scatter plot that that has a color bar with different sizes
# and the the plot have to be a triangle instead of a circle.

x = np.random.randint(100,size=(50))
y = np.random.randint(100,size=(50))
colors = np.random.randint(100,size=(50))
sizes = 15 * np.random.randint(100,size=(50))


plt.scatter(x,y,c=colors,s=sizes,cmap='jet',alpha=0.5,marker='*')
plt.colorbar()
plt.show()

# Create a list called rocnation sales, using the album sales that
# was displayed for Rihanna,Kanye,J.cole,and Wale.
# Find the total average,median,variance,and standard deviation of all 4 of those artist sales.

avg_sales = np.average(sales)
median = np.median(sales)
variance = np.var(sales)
std_dev = np.std(sales)

print(f'Average is {avg_sales}')
print(f'Median is {median}')
print(f'Variance is {variance}')
print(f'Standard Deviation is {std_dev}')