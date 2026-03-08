from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = ((df['nombre'] == 'Carlos') & (df['ciudad'] == 'Cali')).sum()

print(cantidad)