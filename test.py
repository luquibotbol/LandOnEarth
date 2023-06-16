import time
import pandas as pd
import csv

csv1 = "agents.csv"
csv2 = "empty.csv"
df = pd.read_csv(csv1)
ds = pd.read_csv(csv2)

count = 0
for x in range(len(ds)):
    # Add to lower here somewhere
    row = df.loc[(df['FIRST'] == ds["FIRST"][x]) & (df['LAST'] == ds["LAST"][x] )].values
    if (len(row)>0):
        print(df.loc[(df['FIRST'] == ds["FIRST"][x]) & (df['LAST'] == ds["LAST"][x] )].values[0][0])
        count +=1
        # for item in row[0]:
        #     print(item)
    else:
        print("------ERROR------", ds["FIRST"][x], ds["LAST"][x])

# print(df.loc[(df['FIRST'] == ds["FIRST"][1]) & (df['LAST'] == ds["LAST"][1] )].values[0][0])
print(count)