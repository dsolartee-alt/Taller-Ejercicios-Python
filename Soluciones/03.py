from utils import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df[df['nombre'] == 'Juan'].shape[0]

print(cantidad)