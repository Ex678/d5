import pandas as pd
import os

df = pd.read_csv("./amazon_prime_titles.csv")
#print(df)

columnas = df.columns
indices = df.index
num_filas = df.shape[0]

print(columnas)
print(indices)
print(num_filas)