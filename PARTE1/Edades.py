edadStr= input("Ingrese su edad (0-120): ")
edad=int(edadStr)
nombre= input("Ingrese su nombre: ")

if edad >= 0 and edad <= 12:
    print(f"{nombre} eres un niño")
elif edad >= 13 and edad <= 17:
    print(f"{nombre} eres un adolescente")
elif edad >= 18 and edad <= 30:
    print(f"{nombre} eres un adulto joven")
elif edad >= 31 and edad <= 60:
    print(f"{nombre} eres un adulto injoven")
elif edad >= 61 and edad <= 120:
    print(f"{nombre} eres un adulto mayor")
else:
    print("Su edad es incorrecta, a menos que sea un vampiro!!")