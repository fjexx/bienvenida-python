def determinarResultadosIMC()

if imc >= 0 and imc <16:
    print("Usted tiene delgadez severa.")
elif imc >= 16 and imc <17:
    print("Usted tiene delgadez moderada.")
elif imc >= 17 and imc <18.5:
    print("Usted tiene delgadez leve.")
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