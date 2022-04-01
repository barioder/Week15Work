import cv2
import pandas as pd
img = cv2.imread("E:\Entertainment\MOVIES\Flora Ulysses (2021) [720p] [WEBRip] [YTS.MX]\www.YTS.MX.jpg", 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)

# 1.Create a dictionary called test scores, the keys is the name and values is there grades for 3
# classes. Turn that dictionary to a pandas Series.

test_results = {'A': [25, 26, 50, 70],
                'B': [31, 45, 60, 75]}

test_series = pd.Series(test_results)

print(test_series)

# 2.Download any data online and transform that csv file from rows to columnns.

data_df = pd.read_csv("E:/Education/aws/class/Week 17/WHO-COVID-19-global-table-data.csv")
print(data_df)
print('----------------------------')
df = data_df.transpose()

print(df)

# 3.Download a picture and find out the shape of that picture.


