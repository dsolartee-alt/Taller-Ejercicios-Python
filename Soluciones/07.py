from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df[df['ciudad'] == 'Medellin'].shape[0]

print(cantidad)