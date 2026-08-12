# Ejercicio 4: Recorre la lista "notas" y encuentra la nota 
# más alta SIN usar la función max()
notas = [3.5, 4.2, 2.8, 4.8, 3.9]
mayor = 0
for nota in notas:
    if nota > mayor:
        mayor = nota
print(mayor)