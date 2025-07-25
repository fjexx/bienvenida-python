nombreProducto= input("Ingrese el nombre de un producto: ")
precioProducto= input("Ingrese el precio de un producto: ")
cantidad= input("Ingrese la cantidad de productos que quiere comprar: ")

precioProductoFloat= float(precioProducto)
cantidadEntero= int(cantidad)

total= precioProductoFloat*cantidadEntero

print(f"El valor de {cantidadEntero} de {nombreProducto} es {total}")