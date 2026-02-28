import pandas as pd

# Cargar dataset SIN limpiar
df = pd.read_csv('data/personas.csv')

# Convertir id a texto
df['id'] = df['id'].astype(str)

# Contar ids que tengan caracteres NO numéricos
cantidad = df['id'].str.contains(r'[^0-9]').sum()

print(cantidad)