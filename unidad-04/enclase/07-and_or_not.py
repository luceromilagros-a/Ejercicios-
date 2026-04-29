### not ###


# and


from hashlib import algorithms_available

alumno_edad = int(input("Inserte la edad del alumno: "))


if alumno_edad > 40 and alumno_edad < 50:
    # acá empieza bloque de codigo si la condicion de arriba es True
    print("el alumno es mayor de 40 años y menor de 50 años")
elif alumno_edad >= 30 and alumno_edad < 40:
    # bloque de codigo
    print("el alumno es mayor de 30 años y menor de 40 años")


else:
    print("el alumno es menor de 30 años")

print("Fin del programa")


exit()

numero = 5

if numero > 0 and numero % 2 == 0:
    print("El número NO es igual a cero.")
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
else:
    print("El número es igual a cero.")
