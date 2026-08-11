notas = []
continuar = "s"

while continuar == "s":
    nota = float(input("Ingresa una nota: "))
    notas.append(nota)
    continuar = input("¿Agregar otra nota? (s/n): ")

promedio = sum(notas) / len(notas)
if promedio >= 4:
    print(f'Su promedio fue de: ',promedio, 'desempeño increible, sigue asi')
elif promedio >= 3:
    print(f'Su promedio fue de: ',promedio, 'desempeño regular')
else:
    print(f'Su promedio fue de: ',promedio, 'perdiste el semestre')