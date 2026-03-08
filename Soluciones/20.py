from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

df['fecha_nacimiento'] = df['fecha_nacimiento'].dt.year

cantidad = ((df['fecha_nacimiento'] >= 1990) & (df['fecha_nacimiento'] <= 2000)).sum()

print(cantidad)