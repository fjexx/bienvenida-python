def calcularPromedio(nota1, nota2, nota3):
    totalNotas= (nota1+nota2+nota3)/3
    return totalNotas

def consultarMulta(tipoMulta):
    if tipoMulta==1:
        tipoMulta= 10
        return tipoMulta
    elif tipoMulta==2:
        tipoMulta= 15
        return tipoMulta
    elif tipoMulta==3:
        tipoMulta= 20
        return tipoMulta
    elif tipoMulta==4:
        tipoMulta= 30
        return tipoMulta
    elif tipoMulta==0:
        tipoMulta= -1
        return tipoMulta
    elif tipoMulta==5:
        tipoMulta= -1
        return tipoMulta


def calcularValorHora(salario):
    totalSalario= salario/160
    return totalSalario
    
def calcularSubtotal(precioProductoStr, cantidadStr, porcentajeDescuentoStr):
    precioProducto=float(precioProductoStr)
    cantidad= int(cantidadStr)
    porcentajeDescuento= float(porcentajeDescuentoStr)

    subtotalSinDescuento= precioProducto*cantidad
    descuento= (subtotalSinDescuento*porcentajeDescuento)/100
    descuento= subtotalSinDescuento-porcentajeDescuento
    return descuento

def calcularValorDescuento(precioStr, porcentajeDescuentoStr):
    precio= float(precioStr)
    porcentajeDescuento= float(porcentajeDescuentoStr)

    return porcentajeDescuento

