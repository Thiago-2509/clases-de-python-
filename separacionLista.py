# Ejercicio 7: Separa la lista "numeros_mixtos" en dos listas 
# nuevas: "pares" e "impares"
numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for numero in numeros_mixtos:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Pares:',pares)
print(f'impares:',impares)