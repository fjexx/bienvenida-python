def mostrarInfo(nombre, apellido, anioNacimiento):
    import datetime
    fechaHoy= datetime.date.today()
    anioActual= fechaHoy.year
    edad= anioActual - anioNacimiento
    print(f"{nombre} {apellido} este año cumple {edad} años")