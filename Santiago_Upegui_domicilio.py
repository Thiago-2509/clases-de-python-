#====================
#Sistema de domicilio
#====================
# Aqui se ingresa el dato y con float se comvierte en decimal
continuar = 's'
while(continuar == 's'):

    distance_Km = float(input('Ingrese la distancia en km: '))

    print(f'distancai en km:  {distance_Km}')

    #Estas son las condiciones de el domicilio si es mayor o igal a tres muestra un valor y si es mayor o igual a 8 muestra otro valor. Si se pone una distancia mayor a 8 se muestr un mensaje que diga que no se cubre tanta distancia 
    if distance_Km <= 3:
        costo_domicilio = 3000
    elif distance_Km <= 8:
        costo_domicilio = 7000
    else:
        costo_domicilio = 0

    if costo_domicilio == 0:
        print('Por fuera del area. No hay domicilio')
    else:
        print(f'El costo del domicilio es de: ${costo_domicilio}')  

    continuar = input('Realizar otro calculo (s/n): ')
print('Gracias por utilizar el sistema')
        