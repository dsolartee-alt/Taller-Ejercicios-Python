from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = (df['activo'] == False).sum()

print(cantidad)