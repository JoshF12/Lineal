# cual es la moda de todas las notas

import pandas as pd
from statistics import mode
from Estudiantes import estudiantes

df = pd.DataFrame(estudiantes)

# Filtrar estudiantes que tengan exactamente 3 notas
df = df[df["notas"].apply(lambda x: isinstance(x, list) and len(x) == 3)]

# Unir todas las notas en una sola lista
todas_las_notas = sum(df["notas"], [])

if not todas_las_notas:
    print("La lista de notas está vacía o hay estudiantes sin suficientes notas.")
else:
    try:
        moda = mode(todas_las_notas)
        print("La moda de todas las notas es:", moda)
    except Exception as e:
        print("No se pudo calcular la moda:", e)