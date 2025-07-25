import random

print("Vas a jugar piedra, papel o tijera contra el computador")
print("Para PIEDRA digita 1")
print("Para PAPEL digita 2")
print("Para TIJERA digita 3")

miElecciónStr=input("Escoja una opción: ")
miElección=int(miElecciónStr)
if miElección == 1:
    print("Elegiste PIEDRA")
elif miElección == 2:
    print("Elegiste PAPEL")
elif miElección == 3:
    print("Elegiste TIJERA")
else:
    print("Debe elegir un número entre 1 y 3")

eleccionCompu= random.randint(1, 3)
if eleccionCompu == 1:
    print("La compu eligió PIEDRA")
elif eleccionCompu == 2:
    print("La compu eligió PAPEL")
elif eleccionCompu == 3:
    print("La compu eligió TIJERA")

if miElección == eleccionCompu:
    print("Empate")
elif(miElección == 1 and eleccionCompu == 3) or (miElección == 2 and eleccionCompu == 1 ) or (miElección == 3 and eleccionCompu == 2):
    print("Le ganaste a la compu")
elif (eleccionCompu ==1 and miElección == 3) or (eleccionCompu == 2 and miElección == 1) or (eleccionCompu == 3 and miElección == 2):
    print("Te ganó la compu XDD")