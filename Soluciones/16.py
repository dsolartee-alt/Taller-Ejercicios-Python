from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

ciudades = df['ciudad'].nunique()

print(ciudades)