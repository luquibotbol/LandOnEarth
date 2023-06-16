import time
import pandas as pd
import csv

csv1 = "agents.csv"

df = pd.read_csv(csv1)
print(df.loc[(df['FIRST'] == "ChengDe") & (df['LAST'] == "Yen" )])
