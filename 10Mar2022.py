import numpy as np

from matplotlib import pyplot as plt
# 1.Create a plot graph that have 2 lines intersecting
# and add
# a point to the plot.

# Graph 1
l1 = np.array([10, 25, 40, 55, 60])
l2 = np.array([1, 5, 58, 79, 80])

plt.subplot(2, 2, 1)

plt.plot(l1, marker='o')
plt.plot(l2)
plt.title('Figure 1')

# 2.Create a bar graph displaying a label
# for the y axis and x axis.
# Inside a grid.
x = np.array([10, 20, 30, 40, 50])
y = np.array([25, 50, 10, 80, 76])
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.grid()
plt.xlabel('Age')
plt.ylabel('Number of people')
plt.title('Figure 2')

# 3.Top 5 students pass the exam,create a pie graph of
# the students scores from highest to lowest,
# then find the
# total average of the students.

students = ['Derrick', 'Steven', 'Andrew', 'Rita']
color = ['red', 'yellow', 'blue', 'green']
scores = np.array([70, 60, 55, 40])
plt.subplot(2, 2, 3)

plt.pie(scores, labels=students, colors=color, autopct='%1.1f%%')
plt.title('figure 3')

average_score = np.mean(scores)
print(f'The average score of the students is {average_score}')
# 4.Create a scatter plot displaying any color you desire
# but
# in different sizes and the plot have to be in stars.
# (add a color bar).


# 5.Put question 1,2,3,and 4 graphs in one figure.

plt.show()