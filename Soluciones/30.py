from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = ((df['nombre'] == 'Jose') & (df['apellido'] == 'Garcia')).sum()

print(cantidad)