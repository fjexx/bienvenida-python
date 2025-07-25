estaturaStr= input("Ingrese su estatura en metros: ")
estatura= float(estaturaStr)
if estatura < 0 or estatura > 2.50:
    print("Estatura fuera de rango, ingrese una estatura válida")
    exit()

pesoStr= input("Ingrese su peso en kilogramos: ")
peso= float(pesoStr)
if peso < 0 or peso > 300.0:
    print("Peso fuera de rango.")
    exit()

nombre= input("Ingrese su nombre: ")

imc= peso / (estatura*estatura)
print(f"Su índice de masa corporal es {imc}")

if imc >= 0 and imc <16:
    print(f"{nombre} usted tiene delgadez severa.")
elif imc >= 16 and imc <17:
    print(f" {nombre} usted tiene delgadez moderada.")
elif imc >= 17 and imc <18.5:
    print(f"{nombre} usted tiene delgadez leve.")
elif imc >= 18.5 and imc <25:
    print(f"{nombre} usted tiene peso normal.")
elif imc >= 25 and imc <30:
    print(f"{nombre} usted tiene sobrepeso.")
elif imc >= 30 and imc <35:
    print(f"{nombre} usted tiene Obesidad Grado 1.")
elif imc >= 35 and imc <40:
    print(f"{nombre} usted tiene Obesidad Grado 2.")
elif imc >= 40:
    print(f"{nombre} usted tiene Obesidad Grado 3.")