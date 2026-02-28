from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df[df['nombre'] == 'Maria'].shape[0]

print(cantidad)