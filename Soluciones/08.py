from utils import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = df['ciudad'].nunique()

print(cantidad)