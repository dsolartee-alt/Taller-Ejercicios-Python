from utils import cargar_y_limpiar

df = cargar_y_limpiar()

conteo = df['apellido'].value_counts()

apellido_mas_frecuente = conteo.idxmax()
cantidad = conteo.max()

print(apellido_mas_frecuente, cantidad)