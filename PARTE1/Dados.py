import random
print("**** PRUEBA TU SUERTE ****")
print(" Si obtienes el valor de 6, ganas")
input("Presiona ENTER para lanzar el dado.")

valorObtenido= random.randint(1, 6)

print(f"Obtuviste un {valorObtenido} ")
if valorObtenido == 6:
    print("Felicidades Ganaste!! ")
    print("Estás de suerte!! ")
else: 
    print("Lo siento, no es tu día de suerte") 