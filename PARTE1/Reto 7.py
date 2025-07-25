nombreUsuario= input("Ingrese su nombre: ")
edadUsuario= input("Ingrese su edad: ")

nombreAmigo= input("Ingrese el nombre de un amigo: ")
edadAmigo= input("Ingrese la edad de su amigo: ")

edadUsuarioEntero= int(edadUsuario)
edadAmigoEntero= int(edadAmigo)

sumaEdades= edadUsuarioEntero+edadAmigoEntero
diferenciaEdades= edadUsuarioEntero-edadAmigoEntero

print(f"La suma de las edades de {nombreUsuario} y {nombreAmigo} es {sumaEdades}")
print(f"La diferencia de edades entre {nombreUsuario} y {nombreAmigo} es {diferenciaEdades}")