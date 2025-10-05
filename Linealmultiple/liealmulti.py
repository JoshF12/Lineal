import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

datos = {
    'Superficie_m2': [50, 70, 65, 90, 45],
    'Num_Habitaciones': [1, 2, 3, 3, 1],
    'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0],
    'Precio_UF': [2500, 3800, 3500, 5200, 2100]
}

df = pd.DataFrame(datos)

X = df[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]
y = df['Precio_UF']

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

print("=== Parámetros del modelo ===")
print("Coeficientes:", modelo.coef_)
print("Intercepto:", modelo.intercept_)
print()

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("=== Evaluación del modelo ===")
print("Error cuadrático medio (MSE):", round(mse, 2))
print("Coeficiente de determinación (R²):", round(r2, 2))
print()

nueva_vivienda = [[60, 2, 0.6]]
prediccion = modelo.predict(nueva_vivienda)

print("=== Predicción para una nueva vivienda ===")
print("Superficie: 60 m², Habitaciones: 2, Distancia al metro: 0.6 km")
print("Precio estimado:", round(prediccion[0], 2), "UF")
