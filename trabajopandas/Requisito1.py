# calcular el promedio de cada estudiante y mostrar cual es el max y min (promedio)

import pandas as pd

from Estudiantes import estudiantes

df = pd.DataFrame(estudiantes)

# Filtrar estudiantes que tengan exactamente 3 notas
df = df[df["notas"].apply(lambda x: isinstance(x, list) and len(x) == 3)]

if df.empty:
    print("No hay estudiantes con la cantidad correcta de notas.")
else:
    df["promedio"] = df["notas"].apply(lambda x: round(sum(x) / len(x), 1))
    max_promedio = df["promedio"].max()
    min_promedio = df["promedio"].min()

    print(df)
    print("Promedio máximo:", max_promedio)
    print("Promedio mínimo:", min_promedio)
