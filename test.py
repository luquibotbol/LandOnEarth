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
    row = df.loc[(df['FIRST'] == ds["FIRST"][x].lower()) & (df['LAST'] == ds["LAST"][x].lower())].values
    if (len(row)>0):
        ds.at[x, "LICENSE"] = row[0][3]
        ds.at[x, "EMAIL"] = row[0][4]
        ds.at[x, "PHONE"]= row[0][5]
        

        # for item in row[0]:
        #     print(item)
    else:
        print("------ERROR------", ds["FIRST"][x], ds["LAST"][x])
        count +=1

# print(df.loc[(df['FIRST'] == ds["FIRST"][1]) & (df['LAST'] == ds["LAST"][1] )].values[0][0])
print(count)
print(ds)
ds.to_csv("filled.csv",index=False)

# To format the empty csv on the left and the right
# =LEFT(A1,FIND("-",A1)-1)
