import pandas as pd

df = pd.read_csv('data/personas.csv')

# Comparar original vs versión con strip
cantidad = (df['email'] != df['email'].astype(str).str.strip()).sum()

print(cantidad)