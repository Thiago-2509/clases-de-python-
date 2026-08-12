# --------------------------------------------
# RETO OPCIONAL (para quien quiera ir más allá)
# Usando list comprehension, crea una lista nueva 
# que contenga solo las temperaturas mayores a 20 grados 
# de tu lista "temperaturas" del Ejercicio 1
# --------------------------------------------

temperaturas = []

temperatura1 = int(input('Ingrese la temperatura: '))
if temperatura1 >= 20:
    temperaturas.append(temperatura1)
temperatura2 = int(input('Ingrese la temperatura: '))
if temperatura2 >= 20:
    temperaturas.append(temperatura2)
temperatura3 = int(input('Ingrese la temperatura: '))
if temperatura3 >= 20:
    temperaturas.append(temperatura3)
for temperatura in temperaturas:
    print(temperatura)