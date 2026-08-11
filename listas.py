# ============================================
# EJERCICIOS - Listas en Python
# Escribe tu código debajo de cada enunciado
# ============================================

# --------------------------------------------
# ACTIVIDAD 1: Explica con tus palabras qué hace 
# cada línea, agregando un comentario arriba de cada una
# --------------------------------------------

#Se esta creando una lista la cual esta vacia
notas = []
#Se le pide al usuario que agregue su nota (numero el cual se convierte en float) 
nota1 = float(input("Ingresa una nota: "))
#.append sirve para agregar datos ingresados por el usuario la lista vacia (Se agregan siempre al final de la lista)
notas.append(nota1)
#Un print que muestra la lista ya con el dato del usuario agregado 
print(f"Total de notas: {notas}")

