import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definición de la función de integración por regla del trapecio
def integracion_trapecio(x, y):
    n = len(x) - 1  # Cantidad de subintervalos
    a = x[0]  # Límite de integración inferior
    b = x[n]  # Límite de integración superior
    
    # Cálculo de la integral usando la fórmula del trapecio
    integral = (y[0] + 2 * sum(y[1:n]) + y[n]) * (b - a) / (2 * n)
    
    return integral

# Cargar los datos desde un archivo Excel
# Asegúrate de que el archivo Excel tiene dos columnas, una para 'x' y otra para 'y'
archivo_excel = r'C:\Users\alexc\Videos\CEA_M_Total_First_1000.xlsx'  # Ruta completa con 'r'
df = pd.read_excel(archivo_excel)

# Extraer los valores de las columnas de x y y
x = df.iloc[:, 0].values  # Primera columna (x)
y = df.iloc[:, 1].values  # Segunda columna (y)

# Asegurarnos de que hay suficientes datos
if len(x) < 1000 or len(y) < 1000:
    raise ValueError("El archivo debe contener al menos 1000 datos en ambas columnas.")

# Usar solo los primeros 1000 datos
x = x[:1000]
y = y[:1000]

# Calcular la integral usando la regla del trapecio
resultado = integracion_trapecio(x, y)

# Mostrar el resultado de la integración
print(f"El resultado de la integración por el método del trapecio es: {resultado:.6f}")

# Crear gráfico mostrando los trapecios
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b', label="Datos")
plt.fill_between(x, y, alpha=0.3, color='lightblue', label=f"Área aprox. (Trapecio): {resultado:.6f}")
plt.scatter(x, y, color='red')  # Marcar los puntos donde se calculan los trapecios

# Agregar líneas verticales que representan los trapecios
for i in range(len(x)-1):
    plt.plot([x[i], x[i]], [0, y[i]], 'k--', alpha=0.6)  # Línea desde el eje x a la función

# Etiquetas y leyenda
plt.title("Integración por el método del trapecio usando 1000 datos", fontsize=15)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)

# Mostrar el gráfico
plt.show()
