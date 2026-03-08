from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = (df['activo'] == True).sum()

print(cantidad)