from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df['profesion'].nunique()

print(cantidad)