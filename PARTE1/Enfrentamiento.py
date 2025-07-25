import random

nombreJugador1= input("Jugador 1, ingrese su nombre: ")
nombreJugador2= input("Jugador 2, ingrese su nombre: ")

input("Jugador 1, presione ENTER para lanzar el dado.")
lanzamientoJugador1= random.randint(1, 6)
print(f"{nombreJugador1} sacaste un {lanzamientoJugador1}")

input("Jugador 2, presione ENTER para lanzar el dado.")
lanzamientoJugador2= random.randint(1, 6)
print(f"{nombreJugador2} sacaste un {lanzamientoJugador2}")

if lanzamientoJugador1 > lanzamientoJugador2:
    print(f"El ganador es {nombreJugador1}.")
elif lanzamientoJugador1 < lanzamientoJugador2:
    print(f"El ganador es {nombreJugador2}.")
else:
    print(f"{nombreJugador1} y {nombreJugador2} empataron.")

