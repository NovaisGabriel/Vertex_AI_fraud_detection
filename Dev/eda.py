import pandas as pd
import numpy as np

df = pd.read_csv("./data/creditcard.csv")
print(df.info())
print(df.head())

df.describe()