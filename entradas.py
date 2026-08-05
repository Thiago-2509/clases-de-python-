#--------------------
#SISTEMA DE ENTRADAS
#--------------------

edad = int(input('Ingrese su edad: '))
fechaCompra = int(input('Hace cuantos dias compro su entrada: '))

if edad >= 18 and fechaCompra >= 7:
    print('Acceso VIP')
elif edad >= 18 or fechaCompra >= 7:
    print('Acceso general')
elif edad < 18 and fechaCompra < 7:
    print('Acceso denegado')
  