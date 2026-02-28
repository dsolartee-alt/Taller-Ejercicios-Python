import pandas as pd

df = pd.read_csv('data/personas.csv')

df['salario'] = df['salario'].astype(str)

cantidad = df['salario'].str.contains(r'[^0-9]').sum()

print(cantidad)