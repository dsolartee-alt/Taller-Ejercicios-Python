from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df['email'].str.contains('gmail.com').sum()

print(cantidad)