import pandas as pd

df = pd.read_excel("ventas.xlsx")  # Lee el archivo Excel
print(df.head())  # Imprime los datos del archivo

"""Analisis de datos"""

print(f"Tengo registros de {df.shape[0]} y columnas {df.shape[1]}")
print(df.info())