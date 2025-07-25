import random
print("**** Debes obtener más de 8 para salvarte ****")
input("Presiona ENTER para lanzar el dado.")

valorDado1= random.randint(1, 6)
valorDado2= random.randint(1, 6)
total= valorDado1 + valorDado2

print(f"Ha obtenido {valorDado1} y {valorDado2}, total {total}")
if total < 8:
    print(" Lo siento no es tu día de suerte, no te salvas ")
else: 
    total >= 8
    print("Te salvaste!!")