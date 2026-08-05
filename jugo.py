jugo = 5000
agua = 2500
cola = 5500
print('''Opciones:
      1. Agua: 2500
      2. Jugo: 5000
      3. Cola: 5500''')
opcion = int(input('Que desea comprar (1-3): '))
if opcion < 1 or opcion > 3:
    print('Opcion no valida')
    dinero = int(input('Ingrese su dinero'))

if opcion == 1:
    precio = agua
    producto = 'agua'
elif opcion == 2:
    precio = jugo
    producto = 'jugo'
elif opcion == 3:
    precio = cola
    producto = 'cola'

if dinero >= precio:
    cambio = dinero - precio 
    print(f'{producto} comprado')
    print(f'Su cambio es: {cambio}')
else:
    print('Dinero insuficiente')