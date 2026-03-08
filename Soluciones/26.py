from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = (
    (df['ciudad'] == 'Barranquilla') &
    (df['activo'] == True) &
    (df['fecha_nacimiento'].dt.year > 1980)
).sum()

print(cantidad)