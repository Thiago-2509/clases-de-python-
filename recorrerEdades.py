# Ejercicio 3: Recorre la lista "edades" y cuenta cuántas 
# personas son mayores de edad (18 o más)
edades = [15, 22, 17, 30, 12, 19]
mayor = 0
for edad in edades:
    if edad >= 18:
        mayor += 1

print(mayor)