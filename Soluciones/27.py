from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

ingenieros = df[df['profesion'] == 'Ingeniero']

ciudad = ingenieros['ciudad'].value_counts().idxmax()

print(ciudad)