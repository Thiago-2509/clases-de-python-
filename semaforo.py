continuar = 's'
while(continuar == 's'): 
    estadoSemaforo = input('De que color es el semaforo: ')
    if estadoSemaforo == 'verde':
        print('Los autos pueden pasar')
    elif estadoSemaforo == 'amarillo':
        print('Los autos deben de ir despacio')
    else:
        print('Los carros deben parar')
        
    continuar = input('Desea continuar(s/n): ')
print('gracias')