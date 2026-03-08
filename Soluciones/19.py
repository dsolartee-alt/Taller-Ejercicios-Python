import pandas as pd

df = pd.read_csv('data/personas.csv')

cantidad = df['fecha_nacimiento'].str.contains(r'^\d{4}-\d{2}-\d{2}$') == False

print(cantidad.sum())