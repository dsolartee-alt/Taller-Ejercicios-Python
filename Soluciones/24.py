from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = ((df['nombre'] == 'Ana') & (df['profesion'] == 'Medico')).sum()

print(cantidad)