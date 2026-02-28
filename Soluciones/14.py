from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

promedio = df['salario'].mean()

print(round(promedio, 2))