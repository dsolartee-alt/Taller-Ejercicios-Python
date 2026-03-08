from limpiar import cargar_y_limpiar
import pandas as pd

df = cargar_y_limpiar()

hoy = pd.Timestamp("2026-02-26")

edad = (hoy - df['fecha_nacimiento']).dt.days // 365

cantidad = (edad > 50).sum()

print(cantidad)