
import pandas as pd

# Leer dataset
df = pd.read_csv("datos/sales_sample_2024.csv")

# Mostrar primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Analisis estadistico
promedio = df["sales_amount"].mean()
maximo = df["sales_amount"].max()
minimo = df["sales_amount"].min()
total = df["sales_amount"].sum()

# Crear resumen estadistico
resumen = pd.DataFrame({
    "Promedio": [promedio],
    "Maximo": [maximo],
    "Minimo": [minimo],
    "Total Ventas": [total]
})

# Guardar resultados
resumen.to_csv("resultados/resumen_estadistico.csv", index=False)

print("\nAnalisis completado correctamente")
