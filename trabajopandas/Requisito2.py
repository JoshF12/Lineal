# cuantos estudiantes tienen todas las notas >= 4.0

import pandas as pd
from Estudiantes import estudiantes

df = pd.DataFrame(estudiantes)

# Filtrar estudiantes que tengan exactamente 3 notas
df = df[df["notas"].apply(lambda x: isinstance(x, list) and len(x) == 3)]

if df.empty:
    print("No hay estudiantes con la cantidad correcta de notas.")
else:
    df["aprobados"] = df["notas"].apply(lambda x: all(n >= 4.0 for n in x))
    cantidad_aprobados = df["aprobados"].sum()
    print("Cantidad de aprobados (todas las notas>=4,0):",cantidad_aprobados)