from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

cantidad = ((df['profesion'] == 'Abogado') & (df['salario'] > 10000000)).sum()

print(cantidad)