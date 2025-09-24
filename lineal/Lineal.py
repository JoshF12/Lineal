import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Leer CSV con datos reales
df = pd.read_csv("partidos_u_de_chile.csv")

# Variables independientes (X) y dependiente (y)
X = df[['remates', 'posesion', 'tiros_arco', 'corners', 'faltas']]
y = df['goles_u']

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Evaluación
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Resultados de la Evaluación:")
print(f"RMSE: {rmse:.2f} (En promedio, las predicciones se desvían en {rmse:.2f} goles)")
print(f"R²: {r2:.0%} (El modelo explica el {r2:.0%} de la variación en los goles)")
