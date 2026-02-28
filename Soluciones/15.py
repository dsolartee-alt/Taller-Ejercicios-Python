from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

maximo = df['salario'].max()

print(int(maximo))