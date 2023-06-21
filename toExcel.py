import time
import pandas as pd
import csv

csv1 = "agents.csv"
csv2 = "empty.csv"
df = pd.read_csv(csv1)
ds = pd.read_csv(csv2)

# linkstr = "" # Put all the links in here
# links = linkstr.split(",")

count = 0
for x in range(len(ds)):
    row = df.loc[(df['FIRST'] == ds["FIRST"][x].lower()) & (df['LAST'] == ds["LAST"][x].lower())].values
    if (len(row)>0):
        ds.at[x, "LICENSE"] = row[0][3]
        ds.at[x, "EMAIL"] = row[0][4]
        ds.at[x, "PHONE"]= row[0][5]
        ds.at[x, "PASSWORD"] = ds["FIRST"][x][0] + ds["LAST"][x][0] + "exp2023" # Add extra password in this string
        ds.at[x, "BROKERAGE"] = "eXp Realty" # Add Brokerage Name
        ds.at[x, "BROKER"] = "Tony King" # Add Broker Name
        
        # # Test stuff
        # ds.at[x, "BLACK URL"] = links[x]
        # ds.at[x, "PROD URL"] = links[x].replace(".black", ".com")


    else:
        # print individual errors
        ds.at[x, "PASSWORD"] = ds["FIRST"][x][0] + ds["LAST"][x][0] + "exp2023" # Add extra password in this string
        ds.at[x, "BROKERAGE"] = "eXp Realty" # Add Brokerage Name
        ds.at[x, "BROKER"] = "Tony King" # Add Broker Name
        print("------ERROR------", ds["FIRST"][x], ds["LAST"][x])
        count +=1

# print total errors
print(count)

ds.to_csv("filled.csv",index=False)

# To format the empty.csv on the left and the right
# =LEFT(A1,FIND(" ",A1)-1)
# =LOWER(A1)
# Then copy the values and paste it with the 123 thingy
