import random
print("Lanza un dado para ver las distintas penitencias")
input("Presiona ENTER para lanzar el dado.")

valorObtenido= random.randint(1, 6)

print(f"Obtuviste un {valorObtenido} ")
if valorObtenido == 1:
    print("Haz 10 abdominales ")
if valorObtenido == 2:
    print("Aguanta la respiración por 2 minutos ")
if valorObtenido == 3:
    print("Haz 15 sentadillas ")
if valorObtenido == 4:
    print("Camina 20 pasos agachado ")
if valorObtenido == 5:
    print("Haz 15 lagartijas ")
if valorObtenido == 6:
    print("Comunícate con alguien sin hablarle")