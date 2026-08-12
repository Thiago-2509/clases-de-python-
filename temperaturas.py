# --------------------------------------------
# EJERCICIO 1
# Crea una lista vacía llamada "temperaturas".
# Pide 3 temperaturas al usuario (una por una) y 
# agrégalas a la lista. Al final, imprime la temperatura 
# más alta y la más baja (usa max() y min())
# --------------------------------------------

#Se creo la lista temperaturas vacia 
temperaturas = []
#Se crearon tres variables (temperatura1,2,3) en las cuales el usuario agrega las teperaturas y con .append se agrega a la lista
temperatura1 = float(input('Ingrese la primer temperatura: '))
if temperatura1 >= 20:
    temperaturas.append(temperatura1)
elif temperatura1 < 20:
    print('No se admiten temperaturas menores a 20 grados')
temperatura2 = float(input('Ingrese la segunda temperatura: '))
if temperatura2 >= 20:
    temperaturas.append(temperatura2)
elif temperatura2 < 20:
    print('No se admiten temperaturas menores a 20 grados')
temperatura3 = float(input('Ingrese la tercer temperatura: '))
if temperatura3 >= 20:
    temperaturas.append(temperatura3)
elif temperatura3 < 20:
    print('No se admiten temperaturas menores a 20 grados')
#Se crea un print en el cual indique la temperatura maxima(max) y la temperatura minima(min) que hay en la lista 
print(f'La temperatura mas alta es: ', max(temperaturas))
print(f'La temperatura mas alta es: ', min(temperaturas))
for temperatura in temperaturas:
    print(temperatura)