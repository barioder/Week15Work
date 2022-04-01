import cv2
import pandas as pd
# 1. Download a picture image and make that image smaller than the original size.
# The image also have to be grey scale.
img = cv2.imread("E:/Education/aws/class/Week 18/www.YTS.MX.jpg")
print(img.shape)
img_new = cv2.resize(img, (250, 250))
print(img_new.shape)

gray_scale = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray_scale', gray_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2.Create a data frame by downloading a csv file and add a new column to your dataFrame.


# 3.In your dataframe i want to know the total average of 3 columns.
# 4. The picture image you downloaded i want you to slice through the second column.
