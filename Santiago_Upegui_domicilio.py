#====================
#Sistema de domicilio
#====================
#Se agrega una variable y un while que sea 's' para que se puedan hacer varios calculos si el cliente lo decea y cuando se ingrese 'n' cierre el programa
continuar = 's'
while(continuar == 's'):
    #Se agrega la variable distance_Km como float para asi poder agregar la distancia del domicilio, se hace en float para mas exactitud seguido de un print que diga la distancia agregada
    distance_Km = float(input('Ingrese la distancia en km: '))

    print(f'distancai en km:  {distance_Km}')

    #Se agregan las condiciones planteadas para realizaar el calculo del domicilio creando una variable costo_domicilio para definir el precio, llegado el caso se ponga una distancia mayor la variable costo_domicilio valdra cero
    if distance_Km <= 3:
        costo_domicilio = 3000
    elif distance_Km <= 8:
        costo_domicilio = 7000
    else:
        costo_domicilio = 0
    #Se hace otra condicion para decir el precio del domicilio y si costo_domicilio vale cero un print que diga 'Por fuera del area. No hay domicilio'
    if costo_domicilio == 0:
        print('Por fuera del area. No hay domicilio')
    else:
        print(f'El costo del domicilio es de: ${costo_domicilio}')  
    #Se finaliza cerrando el while creando una variable continuar donde el usuario pueda decidir si hacer otro domicilio o no, si se pone no saldra un print que diga 'Gracias por utilizar el sistema'
    continuar = input('Realizar otro calculo (s/n): ')
print('Gracias por utilizar el sistema')
        