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
temperaturas.append(temperatura1)
temperatura2 = float(input('Ingrese la segunda temperatura: '))
temperaturas.append(temperatura2)
temperatura3 = float(input('Ingrese la tercer temperatura: '))
temperaturas.append(temperatura3)
#Se crea un print en el cual indique la temperatura maxima(max) y la temperatura minima(min) que hay en la lista 
print(f'La temperatura mas alta es: ', max(temperaturas))
print(f'La temperatura mas alta es: ', min(temperaturas))
for temperatura in temperaturas:
    print(temperatura)