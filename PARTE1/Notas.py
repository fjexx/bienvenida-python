notaExamenStr= input("Ingrese su nota del examen (1-10): ")
notaExamen= int(notaExamenStr)
if notaExamen <= 10 and notaExamen >= 0:
    print("Es una nota válida")
    inasistenciasStr= input("Ingrese cuántas veces ha faltado a clases: ")
    inasistencias=int(inasistenciasStr) 
    if inasistencias < 3 and notaExamen >= 8:
        print("Aprobado")
    else:
        print("Reprobado")
    
else:
    print("Solo se permiten notas entre 1 y 10.")
    
print("FIN DEL PROGRAMA")