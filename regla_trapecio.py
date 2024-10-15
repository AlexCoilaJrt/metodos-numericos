from flask import Flask, request, send_file
from flask_cors import CORS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde otro origen (React frontend)

# Función para procesar la integración
def integracion_trapecio(x, y):
    n = len(x) - 1
    a = x[0]
    b = x[n]
    integral = (y[0] + 2 * sum(y[1:n]) + y[n]) * (b - a) / (2 * n)
    return integral

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file provided", 400

    file = request.files['file']
    df = pd.read_excel(file)

    # Asegurarse de que el archivo tiene al menos dos columnas
    if df.shape[1] < 2:
        return "El archivo debe tener al menos dos columnas", 400

    # Obtener los primeros 1000 valores de las columnas x e y
    x = df.iloc[:1000, 0].values
    y = df.iloc[:1000, 1].values

    # Calcular el área por el método del trapecio
    resultado = integracion_trapecio(x, y)

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b', label="Datos")
    plt.fill_between(x, y, alpha=0.3, color='lightblue', label=f"Área aprox. (Trapecio): {resultado:.6f}")
    plt.scatter(x, y, color='red')
    plt.title("Integración por el método del trapecio usando 1000 datos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico en un objeto en memoria
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
