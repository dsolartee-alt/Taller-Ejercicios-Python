from utils import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df[df['ciudad'] == 'Bogota'].shape[0]

print(cantidad)