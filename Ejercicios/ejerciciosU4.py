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
# ✅ Bien hecho: el while True con isdigit() es una buena forma de forzar entrada numérica.
# 💡 Sugerencia: isdigit() NO acepta números negativos (el "-" no es dígito). Para este ejercicio quizás está bien,
#                pero tenelo presente para casos donde quieras permitir negativos.

if valor_usuario < valor_min :
    print ("VALOR BAJO")
elif valor_usuario < valor_min :
    print ("VALOR ALTO")
# ❌ Error LÓGICO: la condición del elif es la MISMA que la del if (`< valor_min`). ¡Nunca se va a cumplir!
#                 Debería ser:  elif valor_usuario > valor_max :
# 💡 Sugerencia: revisar atentamente las condiciones cuando copiás líneas similares. Errores así de "copy-paste" son comunes.
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
# ✅ Bien hecho: la regla de los bisiestos es notoriamente difícil y la condición compuesta está perfecta.
#                Múltiplos de 4, salvo múltiplos de 100, salvo múltiplos de 400 → todo cubierto.

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
# ✅ Bien hecho: validación con while hasta que inicio < final. ¡Excelente!

while inicio < final :
    print (f"Este es el Bucle número {inicio}")
    inicio += 1
print ("FIN DEL PROGRAMA")
# 💡 Sugerencia: leyendo el ejemplo del enunciado ("bucle número 1, 2, 3..."), pareciera que se espera
#                un contador empezando en 1, no en `inicio`. Si el usuario entra inicio=5 y final=8,
#                tu código imprime "Bucle número 5, 6, 7" en lugar de "1, 2, 3".
#                Si lo querés desde 1, podés llevar un contador aparte:
#                    contador = 1
#                    while inicio < final:
#                        print(f"Este es el bucle número {contador}")
#                        inicio += 1
#                        contador += 1
# 💡 Sugerencia: para iterar entre dos números, en general se prefiere `for i in range(inicio, final)`.

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
# ✅ Bien hecho: muy bien resuelta la lógica anidada (cursada → final → resultado).
# 💡 Sugerencia: la consigna pide AVISAR el promedio antes del veredicto. Te conviene agregar:
#                print(f"Tu promedio es: {promedio}")

"""
5)Escriba un programa que pida los coeficientes de una ecuación de 
primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, 
tener una solución única, o que todos los números sean solución. Se 
recuerda que la fórmula de las soluciones es x = -b / a
Estos son algunos ejemplos de posibles respuestas (el orden de los 
ejemplos no tiene por qué corresponder con el orden de las condiciones):

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 3
La ecuación no tiene solución.

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 4.2
Escriba el valor del coeficiente b: 21
La ecuación tiene una solución: -5.0

ECUACIÓN A X + B = 0
Escriba el valor del coeficiente a: 0
Escriba el valor del coeficiente b: 0
Todos los números son solución.
"""
print ("ECUACIÓN a x + c = 0")
a = float (input (" Ingresá el valor del coeficiente a: "))
b = float (input ("Ingresá el valor del coeficiente b: "))
if a == 0 and b == 0 :
    print ("Todos los números son solución")
elif a == 0 :
    print ("La ecuación no tiene solución")
else :
    x = -b / a
    print (f"La eciación tiene solución: {x}")
# ✅ Bien hecho: los tres casos (a≠0 / a=0,b≠0 / a=0,b=0) están cubiertos en el orden correcto.
# 💡 Sugerencia: typo → "eciación" debería ser "ecuación". Y ojo: el título dice "a x + c = 0" pero los coeficientes
#                que pedís son a y b (mejor unificar).

"""
6)Escriba un programa que pida los coeficientes de una 
ecuación de segundo grado (a x² + b x + c = 0) y 
escriba la solución.

Se recuerda que una ecuación de segundo grado puede 
no tener solución, tener una solución única, tener dos 
soluciones o que todos los números sean solución. Se 
recuerda que la fórmula de las soluciones cuando hay dos 
soluciones es x = (-b ± √(b2-4ac) ) / (2a)

Estos son algunos ejemplos de posibles respuestas (el 
orden de los ejemplos no tiene por qué corresponder con el 
orden de las condiciones).

a	b	c	Solución
1	-2	2	Sin solución real
2	-7	3	Dos soluciones: 0.5 y 3.0
1	2	1	Una solución: -1.0
0	0	5	Sin solución
0	0	0	Todos los números son solución
0	3	2	Una solución: -0.666...
"""
import math

print ("ECUACIÓN a x² + b x + c = 0")
a = float (input ("Ingresá el valor del coeficiente a: "))
b = float (input ("Ingresá el valor del coeficiente b: "))
c = float (input ("Ingresá el valor del coeficiente c: "))
if a == 0 and b == 0 and c == 0 :
    print ("Todos los números son solución")
elif a == 0 and b == 0 :
    print ("Sin solución")
elif a == 0 :
    x = -c / b 
    print (f"Tiene una solución: {x}")
else :
    d = b**2 - 4*a*c
    if d < 0:
        print ("Sin solución real.")
    elif d == 0:
        x = -b / (2 * a)
        print (f"Una solución: {x}")
    else :
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print (f"Dos soluciones: {x1} y {x2}")
# ✅ Bien hecho: ¡un ejercicio que cubre TODOS los casos especiales! a=0/b=0/c=0, a=0/b=0, a=0, discriminante <,=,>.
#                Excelente uso de math.sqrt y muy buena estructura de if anidados. 💪

"""
7)Escriba un programa que pregunte primero 
si se quiere calcular el área de un triángulo 
o la de un círculo. Si se contesta que se quiere 
calcular el área de un triángulo (escribiendo T o t), 
el programa tiene que pedir entonces la base y la altura 
y escribir el área. Si se contesta que se quiere calcular 
el área de un círculo (escribiendo C o c), el programa 
tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura 
dividido por 2 y que el área de un círculo es Pi 
(aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.

"""
PI = 3.14
# 💡 Sugerencia: el enunciado pide usar PI = 3.141592 (más preciso). Acá lo dejaste en 3.14.

print ("CÁLCULO DE ÁREAS")
respuesta = input ("¿Querés calcular el área " \
"de un Triángulo(T) o de un Circulo(C)?" \
"Ingresá la letra de opción elegida: ").upper()
# ✅ Bien hecho: el .upper() permite aceptar tanto "t" como "T" sin escribir dos condiciones. ¡Buena!
if respuesta == "T" :
    base = float (input ("Ingresá la base: "))
    altura = float ("Ingresá la altura: ")
    # ❌ Error GRAVE: te falta el input(). Tal como está, intentás convertir a float el string literal
    #                "Ingresá la altura: ", lo que tira ValueError al ejecutar.
    #                Debería ser:  altura = float(input("Ingresá la altura: "))
    area = (base * altura) / 2
    print (f"El área del triángulo es: {area}")
elif respuesta == "C" :
    radio = float (input ("Ingresa el radio: "))
    area = PI * (radio ** 2)
    print (f"El área del circulo es {area}")
else :
    print ("Opción no válida. Por favor, ingresá T o C.")
# ✅ Bien hecho: el flujo y la cobertura de opciones inválidas está bien planteada.

"""
8)Escriba un programa que pida tres números y diga si 
el tercero está más cerca del primero o del segundo.
"""
dat1 = int (input ("Ingresá el primer número entero: "))
dat2 = int (input ("Ingresá el segundo número entero: "))
dat3 = int (input ("Ingresá el tercer número entero: "))
if dat1 > dat3 :
    distancia1 = dat1 - dat3
else :
    distancia1 = dat3 - dat1
if dat2 > dat3 :
    distancia2 = dat2 - dat3
else :
    distancia2 = dat3 - dat2
# ✅ Bien hecho: muy buena resolución manual del valor absoluto con if/else. Funciona perfecto.
# 💡 Sugerencia (más corta): la función abs() te da el valor absoluto y reemplaza el if/else:
#                distancia1 = abs(dat1 - dat3)
#                distancia2 = abs(dat2 - dat3)
if distancia1 < distancia2 :
    print (f"Está más cerca del primero {dat1}")
elif distancia2 < distancia1 :
    print (f"Está más cerca del segundo {dat2}")
else :
    print ("Está a la misma distancia de ambos")
# ✅ Bien hecho: ¡también contemplaste el caso "a la misma distancia"! Detalle que muchos olvidan.

# =====================================================================
#                       DEVOLUCIÓN FINAL — Milagros
# =====================================================================
#
# ¡Felicitaciones, Mili! 🎉 Se nota muchísimo el trabajo y la dedicación
# que pusiste a lo largo de las tres unidades. Llegaste a resolver
# ejercicios complejos (ecuación de segundo grado, identificación del
# tipo de dato, año bisiesto) con una lógica muy sólida. Avanzaste
# sostenido desde lo más básico de la Unidad 2 hasta los bucles de la
# Unidad 4, y eso es un montón de progreso.
#
# 🌟 PUNTOS FUERTES QUE NOTÉ
#
#   1. Manejo claro de condicionales anidados: la ecuación de segundo
#      grado y el cálculo de la cursada/final están muy bien estructurados.
#   2. Uso prolijo de f-strings y conversiones (int, float) para dar
#      formato a los mensajes y procesar las entradas.
#   3. Atención al detalle en casos que suelen olvidarse: división por
#      cero, año bisiesto múltiplo de 400, "misma distancia" en el
#      ejercicio de los tres números, validación de entrada con while.
#
# 🛠️ ÁREAS PARA SEGUIR TRABAJANDO
#
#   1. Releer las condiciones después de copiar/pegar bloques. El bug
#      del Ejercicio 1 de U4 (`elif valor_usuario < valor_min` repetido)
#      y el `float("Ingresá la altura: ")` sin input() del Ejercicio 7
#      son ejemplos de cómo un repaso rápido al final permite cazar
#      esos errores antes de entregar.
#   2. Volver a leer la consigna antes de imprimir. En algunos
#      ejercicios faltó mostrar el resultado pedido (ej. ejercicio 1
#      de U2, o el promedio en el ejercicio 4 de U4). Una buena
#      costumbre: subrayar los verbos de la consigna ("imprimir",
#      "concatenar", "guardar en una variable") y revisar uno por uno.
#
# 💪 Seguí así, Mili: tu código es legible, ordenado y se nota que
# pensás cada problema antes de tirar líneas. Los errorcitos que
# aparecieron son típicos de cuando uno escribe rápido — con un poco
# más de revisión final, vas a entregar trabajos impecables. ¡Éxitos
# con las próximas unidades!  🚀
# =====================================================================