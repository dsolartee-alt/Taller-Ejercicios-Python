from utils import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df[df['profesion'] == 'Ingeniero'].shape[0]

print(cantidad)