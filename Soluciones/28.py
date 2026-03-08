from limpiar import cargar_y_limpiar

df = cargar_y_limpiar()

promedios = df.groupby('profesion')['salario'].mean()

print(promedios.idxmax())