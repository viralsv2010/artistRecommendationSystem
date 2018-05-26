# import csv

# with open('result.csv', 'rU') as f:
#     reader = csv.reader(f)
#     next(reader)     # Skip header row
#     answer = max(column[0].replace(',', '') for column in reader)
# print answer

# import pandas

# data = pandas.read_csv('result.csv', sep=',') 
# df = pandas.DataFrame(data) 
# # max2max2=df[1].nlargest(2)
# print 
# import numpy as np 

# with open('tt.txt', 'w+') as f:
# 	b=np.loadtxt(r'result.csv',dtype=str,delimiter=',',skiprows=1,usecols=(0,))

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('temp.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

col = columns['support']
sorted(col, key=lambda student: student[0])
print col