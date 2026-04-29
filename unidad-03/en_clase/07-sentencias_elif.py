





# sentencias elif

alumno_nombre = "Federico"
alumno_edad = int(input("Ingrese la edad del alumno: "))


if alumno_edad >= 40:
    
    # bloque de codigo
    # print("El alumno", alumno_nombre, "es mayor de 40 años.")
    
    if alumno_edad >= 50:
        print("El alumno", alumno_nombre, "es mayor de 50 años")
    else:
        print("El alumno", alumno_nombre, "está entre 40 y 50 años")




elif alumno_edad >= 30:
    print("El alumno", alumno_nombre, "es mayor o igual de 30 años.")

elif alumno_edad >= 20:
    print("El alumno", alumno_nombre, "es mayor o igual de 20 años.")

else:
    print("El alumno", alumno_nombre, "es menor de 20 años.")





print("Fin del programa.")