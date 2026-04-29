


"""
Escriba un programa que pida un año y que escriba si es bisiesto o no.
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.
"""




anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
    break