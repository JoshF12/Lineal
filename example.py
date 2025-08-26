estudiantes = [
    {"nombre": "Sofía", "notas": [6.5, 7.0, 3.2]},
    {"nombre": "Mateo", "notas": [5.5, 4.0, 6.2]},
    {"nombre": "Valentina", "notas": [3.8, 4.5, 5.0]},
    {"nombre": "Benjamín", "notas": [2.9, 3.5, 4.2]},
    {"nombre": "Isabella", "notas": [6.0, 6.8, 5.5]},
    {"nombre": "Lucas", "notas": [4.5, 4.9, 3.8]},
    {"nombre": "Martina", "notas": [7.0, 6.5, 6.2]},
    {"nombre": "Agustín", "notas": [5.0, 4.2, 4.8]},
    {"nombre": "Camila", "notas": [3.5, 2.8, 4.0]},
    {"nombre": "Santiago", "notas": [6.2, 5.8, 6.5]},
    {"nombre": "Josefa", "notas": [4.0, 4.5, 5.2]},
    {"nombre": "Tomás", "notas": [3.0, 2.5, 4.0]},
    {"nombre": "Florencia", "notas": [6.8, 6.0, 5.9]},
    {"nombre": "Vicente", "notas": [4.8, 5.0, 5.5]},
    {"nombre": "Antonia", "notas": [3.2, 4.1, 4.7]},
    {"nombre": "Emilia", "notas": [6.0, 6.5, 6.8]},
    {"nombre": "Gaspar", "notas": [5.2, 4.7, 3.9]},
    {"nombre": "Amanda", "notas": [2.5, 3.5, 4.0]},
    {"nombre": "Ignacio", "notas": [6.5, 6.0, 5.8]},
    {"nombre": "Trinidad", "notas": [4.5, 4.2, 3.8]},
    {"nombre": "Catalina", "notas": [7.0, 6.8, 6.5]},
    {"nombre": "Joaquín", "notas": [3.5, 4.0, 4.8]},
    {"nombre": "Renata", "notas": [5.9, 5.5, 6.2]},
    {"nombre": "Cristóbal", "notas": [2.8, 3.2, 3.9]},
    {"nombre": "Jose Ignacio", "notas": [6.0, 5.8, 5.5]},
    {"nombre": "Fernanda", "notas": [4.7, 4.2, 4.9]},
    {"nombre": "Maximiliano", "notas": [3.8, 3.5, 2.9]},
    {"nombre": "Paula", "notas": [6.5, 6.2, 6.9]},
    {"nombre": "Sebastián", "notas": [5.0, 4.5, 4.8]},
    {"nombre": "Constanza", "notas": [3.2, 4.0, 3.9]}
]

max_nota = 0
min_nota = 0
aprobados = 0
nota_baja = 0
from statistics import mode

todas_las_notas = []
for nota in estudiantes:
    todas_las_notas.extend(nota["notas"])
    promedio = sum(nota["notas"]) / len(nota["notas"])
    if promedio > max_nota:
        max_nota = promedio
    if min_nota == 0 or promedio < min_nota:
        min_nota = promedio
    if all(n >= 4.0 for n in nota["notas"]):
        aprobados += 1
    if any(q < 4.0 for q in nota["notas"]):
        nota_baja += 1

moda = mode(todas_las_notas)
porcentaje = (nota_baja / len(estudiantes)) * 100

sorted_estudiantes = sorted(
    [(mayor["nombre"], round(sum(mayor["notas"]) / len(mayor["notas"]))) for mayor in estudiantes],
    key=lambda x: x[1],
    reverse=True
)

print("Promedio máximo:", round(max_nota))
print("Promedio mínimo:", round(min_nota))
print("Moda de todas las notas:", round(moda))
print("Aprobados:", aprobados)
print("Con al menos una nota baja:", round(porcentaje), "%")
print("Listado de estudiantes con su promedio (mayor a menor):", sorted_estudiantes)