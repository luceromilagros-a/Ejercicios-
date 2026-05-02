"""
 1)Crear una variable con valor 20 va a ser como referencia el minimo.
Otra con valor de 500, va a ser como referencia el maximo.
Luego pregunta al usuario por un valor, almacenarlo en otra variable, 
forzar a que ponga un numero, sino preguntar repetidamente.
Ese numero transformarlo en integer

Ahora imprimir en pantalla.
Si el numero que puso el usuario es menor que el valor minimo 
definido mostrar el texto VALOR BAJO
Si el numero que puso el usuario es mayor que el valor maximo 
definido mostrar el texto VALOR ALTO
Si el numero que puso el usuario esta entre el valor minimo y 
el valor maximo mostrar el texto VALOR MEDIO
"""
valor_min = 20
valor_max = 500 

while True :
    entrada = input ("Ingresá un valor entero: ")
    if entrada.isdigit () :
        valor_usuario = int (entrada)
        break
    else :
        print ("Entrada no válida. Por favor, ingresá solo números")
if valor_usuario < valor_min :
    print ("VALOR BAJO")
elif valor_usuario < valor_min : 
    print ("VALOR ALTO")
else :
    print ("VALOR MEDIO")

"""
2)Escriba un programa que pida un año y que escriba si es bisiesto o no.
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
aunque los múltiplos de 400 sí.
"""
anio = int (input ("Ingresa año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) :
    print ("El año es bisiesto!")
else :
    print ("El año no es bisiesto.")

"""
3)Pedir al usuario que ingrese un número de inicio del bucle
Pedir al usuario que ingrese un número de fin del bucle
Validar que el número de inicio sea menor al número de fin, 
si no es así volver a pedir los dos números, hasta que ésto sea correcto
Luego de que el usuario ingrese los dos números, mostrar en 
pantalla todos los números que hay entre el número de inicio y el número de fin
De la siguiente manera:
Este es el bucle número 1
Este es el bucle número 2
Este es el bucle número 3
---
Fin del programa.

"""
inicio = int (input ("Ingresa el número del principio de un Bucle: "))
final = int (input ("Ingresá el número final del Bucle: "))
while inicio >= final :
    print ("El número inicial debe ser menor al número final. Por favor, ingresá otro número")
    inicio = int (input ("Ingresa el número del principio de un Bucle: "))
    final = int (input ("Ingresá el número final del Bucle: "))

while inicio < final :
    print (f"Este es el Bucle número {inicio}")
    inicio += 1 
print ("FIN DEL PROGRAMA")

"""
5)Vamos a realizar un programa que nos va a decir la nota promedio 
de un alumno en todo el cuatrimestre.
Dentro del cuatrimestre son 4 examenes y luego un examen final.
La aprobación del cuatrimestre es con nota 6 o mayor de promedio.
Y si el alumno tiene aprobada la cursada (es decir, obtuvo seis o 
más de 6 de promedio en sus 4 examenes, rinde el examen final)
Si el alumno tiene aprobada la cursada y el examen final, entonces 
el alumno aprobó la materia.

Entonces el programa debe preguntar por la nota de cada examen.
En función de las respuestas, primero debe avisar el promedio de las 
4 notas de los examenes.
En caso de que el promedio sea mayor o igual a 6, debe avisar que el 
alumno tiene aprobada la cursada.
En caso de que el promedio sea menor a 6, debe avisar que el alumno no 
tiene aprobada la cursada.
Luego preguntar por nota del final (en caso de que haya aprobado la cursada), 
si es mayor o igual a 6, debe avisar que el alumno aprobó la materia.
En caso de que sea menor a 6, debe avisar que el alumno no aprobó el final de 
la materia, y puede rendir recuperatorio.

"""
exa1 = float (input ("Ingresá la nota de tu primer exámen: "))
exa2 = float (input ("Ingresá la nota de tu segundo exámen:"))
exa3 = float (input ("Ingresá la nota de tu tercer exámen: "))
exa4 = float (input ("Ingresá la nota de tu cuarto exámen: "))
promedio = (exa1 + exa2 + exa3 + exa4) / 4
if promedio >= 6 :
    print ("Aprobaste la cursada!!!. Podes rendir tu exámen final.")
    final = float (input ("Ingresá tu nota del final: "))
    if final >= 6 :
        print ("APROBASTE LA MATERIA!!!!")
    else :
        print ("No aprobaste el final, PERO podes rendir el recuperatorio.")

else :
    print ("Lo siento, no aprobaste la cursada.")

