from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = (df['fecha_nacimiento'].dt.year < 1960).sum()

print(cantidad)