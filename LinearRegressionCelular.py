from sklearn.linear_model import LinearRegression
import numpy as np

antiguedad = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
precio = np.array([3500000, 2800000, 2200000, 1800000, 1449900, 1200000, 900000, 700000, 550000, 400000, 250000])

modelo = LinearRegression()
modelo.fit(antiguedad, precio)

def calcularValor(anios_antiguedad):
    prediccion = modelo.predict([[anios_antiguedad]])
    valor = round(prediccion[0], 2)
    if valor < 0:
        valor = 0
    return valor