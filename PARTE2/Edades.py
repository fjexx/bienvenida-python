import Formatos
print("QUEREMOS CONOCERTE")
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
anioNacimientoStr= input("Ingrese su año de nacimiento: ")
anioNacimiento= int(anioNacimientoStr)

Formatos.mostrarInfo(nombre, apellido, anioNacimiento)