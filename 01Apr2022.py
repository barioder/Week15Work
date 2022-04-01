import numpy as np
import cv2

img = cv2.imread('wts.jpeg')
print(img)

img2 = cv2.imread('wts.jpeg', 0)

# Create a Caesar Cypher using the user input.

cypher_set = 'abcdefghijklmnopqrstuvwxyz'

input_string = input("Enter a string: ")

length_of_string = len(input_string)

string_output = ""

for i in range(length_of_string):
    character = input_string[i]
    location_for_character = cypher_set.find(character)
    new_location = location_for_character + 2
    string_output += cypher_set[new_location]


print(string_output)


# You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
# Create an array of numbers below 100 that are multiples of both 3 and 5, and output it
i = 0
multiples = []
while i <  100 :
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        multiples.append(i)

multiples_array = np.array(multiples)

print(multiples_array)


# Create a data frame call test_scores with 3 columns.
# The columns are Math, Reading ,and Science. Find the mean for all three columns.

import pandas as pd

df = pd.DataFrame({'Math': [75, 65, 66, 80, 90], 'Reading':[80, 70, 86, 90, 60], 'Science': [67, 90, 61, 50, 61]})


columns = ['Math', 'Reading', 'Science']
results = df[columns].mean()

print(results)