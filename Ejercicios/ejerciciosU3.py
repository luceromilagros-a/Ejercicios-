# #1. Solicita al usuario que ingrese su nombre y su edad. 
# #Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".

nombre = input ("Ingresá tu nombre: ")
edad = input ("Ingresá tu edad: ")
print (f"¡Hola, {nombre}! Tienes {edad} años")
# ✅ Bien hecho: muy buen uso del f-string para armar el mensaje.


# # # 2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

# #  +***************+
# #  *               *
# #  *               *
# #  *               *
# #  +***************+

# #  +---+
# #  |   |
# #  |   |
# #  |   |
# #  +---+

# #  ###################################
# #  ###################################
# #  ##                               ##
# #  ##                               ##
# #  ##                               ##
# #  ###################################
# #  ################################### 

print ("+" + "*" * 15 + "+")
print ("*" + " " * 15 + "*")
print ("*" + " " * 15 + "*")
print ("*" + " " * 15 + "*")
print ("+" + "*" * 15 + "+")
print ("Esto es un rectángulo")

print ("+" + "-" * 3 + "+")
print ("|" + " " * 3 + "|")
print ("|" + " " * 3 + "|")
print ("|" + " " * 3 + "|")
print ("+" + "-" * 3 + "+")
print ("Esto es un 'palo'")

print ("##" * 20)
print ("##" * 20)
print ("##" + "  " * 18 + "##")
print ("##" + "  " * 18 + "##")
print ("##" + "  " * 18 + "##")
print ("##" * 20)
print ("##" * 20)
print ("Esto es un 'ladrillo'")
# ✅ Bien hecho: dominás la replicación y concatenación de strings. Las tres figuras quedan bien.
# 💡 Sugerencia: el "ladrillo" usa "##"*20 (40 chars) y para el interior "##" + "  "*18 + "##" (40 chars).
#                Las cuentas te dieron, ¡pero ojo cuando ancho/altura cambien!


# # 3. Solicita al usuario que ingrese dos números enteros. 
# # Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.

nE1 = input ("Ingresá el primer número entero: ")
nE2 = input ("Ingresá el segundo número entero: ")
n1 = float (int (nE1))
n2 = float (int (nE2))
division = n1 / n2
print (f"El resultado de la división es: {division}")
# 💡 Sugerencia: float(int(nE1)) es redundante; alcanza con float(nE1). El doble casteo no aporta nada.
# 💡 Sugerencia: si n2 = 0 el programa rompe con ZeroDivisionError. Lo manejás bien más abajo (ej. 11).


# # 4. Pide al usuario que ingrese una cadena que represente un número entero. 
# # Convierte esta cadena a un entero usando la función int() y luego suma 10. 
# # Imprime el resultado.

cadena = input ("Ingresá un número entero: ")
numero = int (cadena) + 10
print (f"El resultado de la suma es de: {numero}")
# ✅ Bien hecho: conversión y suma resueltas correctamente.

# # 5. Pregunta al usuario que ingrese un número. 
# # Si el número es mayor que 10, imprime "El número es mayor que 10". 
# # Si es igual a 10, imprime "El número es igual a 10". 
# # De lo contrario, imprime "El número es menor que 10".

numero = int (input ("Ingresá un número: "))
if numero > 10:
    print ("El número es mayor a 10")
elif numero == 10:
    print ("El número es igual a 10")
else :
    print ("El número es menor que 10")
# ✅ Bien hecho: el if/elif/else cubre los tres casos con la lógica correcta.
    
# # 6. Solicita al usuario que ingrese dos números y compara si son iguales. 
# # Si lo son, imprime "Los números son iguales". 
# # De lo contrario, imprime "Los números son diferentes".

n1 = input ("Ingresá un número: ")
n2 = input ("Ingresá el segundo número: ")
if n1 == n2:
    print ("Los números son iguales")
else :
    print ("Los número son diferentes")
# 💡 Sugerencia: estás comparando STRINGS. "5" == "5.0" daría False aunque sean el mismo número.
#                Conviene convertirlos antes:  n1 = float(input(...))
# 💡 Sugerencia: typo en el else → "Los número" debería ser "Los números".

# # 7. Pregunta al usuario que ingrese su edad. 
# # Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". 
# # De lo contrario, imprime "Eres menor de edad".

edad = int (input ("Ingresá tu edad: "))
if edad >= 18 :
    print ("Eres mayor de edad")
else :
    print ("Eres menor de edad")
# ✅ Bien hecho: simple y prolijo.

# # 8. Pide al usuario que ingrese una temperatura en Celsius. 
# # Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". 
# # Si es menor o igual a 0, imprime "El agua está congelada". 
# # De lo contrario, imprime "El agua está en estado líquido".

temperaturaC = float (input ("Ingresá la temperatura en Celsius: "))
if temperaturaC >= 100 :
    print ("El agua está hirviendo")
elif temperaturaC <= 0 :
    print ("El agua está congelada")
else :
    print ("El agua está en estado líquido")
# ✅ Bien hecho: usás float (necesario por las temperaturas decimales) y los rangos están bien planteados.

# # 9. Pregunta al usuario que ingrese un número. 
# # Si es positivo, imprime "El número es positivo". 
# # Si es negativo, imprime "El número es negativo". 
# # Si es cero, imprime "El número es cero".

n = int (input ("Ingresá un número:"))

if n > 0 :
    print ("El número es positivo")
elif n < 0 :
    print ("El número es negativo")
else :
    print ("El número es 0")
# ✅ Bien hecho: los tres casos cubiertos correctamente.

# # 10. Solicita al usuario que ingrese un número del 1 al 7. 
# # Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). 
# # Si ingresa un número fuera de ese rango, imprime "Número de día no válido".

num = int (input ("Ingresá un número del 1 al 7: "))
if num == 1 :
    print ("LUNES")
elif num == 2 :
    print ("MARTES")
elif num == 3 : 
    print ("MIÉRCOLES")
elif num == 4 :
    print ("JUEVES")
elif num == 5 :
    print ("VIERNES")
elif num == 6 :
    print ("SÁBADO")
elif num == 7 :
    print ("DOMINGO")
else :
    print ("Número de día no válido")
# ✅ Bien hecho: la cadena de elif funciona bien y el caso "fuera de rango" está cubierto.
# 💡 Sugerencia (avanzada): se podría resolver con una lista o diccionario:
#     dias = ["LUNES","MARTES","MIÉRCOLES","JUEVES","VIERNES","SÁBADO","DOMINGO"]
#     if 1 <= num <= 7: print(dias[num-1])  else: print("Número de día no válido")

# # 11.Calculadora básica
# # Crea un programa que tome dos números como entrada y 
# # luego imprima la suma, resta, multiplicación y división de esos dos números. 
# # Usa operadores aritméticos y asegúrate de manejar casos donde el divisor sea cero.

num1 = int (input ("Ingresá un número entero: "))
num2 = int (input ("Ingresá el segundo número entero: "))
print (f"Suma: {num1 + num2}")
print (f"Resta: {num1 - num2}")
print (f"Multiplicación: {num1 * num2}")
if num2 != 0 :
    print (f"División: {num1 / num2}")
else :
    print ("División: No es posible dividor por cero.")
# ✅ Bien hecho: gran detalle el control de la división por cero. Eso te diferencia.
# 💡 Sugerencia: typo en el mensaje → "dividor" debería ser "dividir".

# # 12.Calculador de IMC
# # Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona. 
# # Pide al usuario su peso en kilogramos y su altura en metros. 
# # Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y 
# # muestra el resultado con un mensaje que indique si el IMC está en el rango normal,
# #  bajo peso, sobrepeso, etc.

peso = float (input ("Ingresá tu peso en kg: "))
altura = float (input ("Ingresá tu altura en metros: "))
imc = peso / (altura ** 2)
print (f"Tu IMC es: {round (imc, 2)}")

if imc < 18.5 :
    print ("Calificación: Bajo peso")
elif 18.5 <= imc < 25 :
    print ("Calificación: Peso normal (saludable)")
elif 25 <= imc < 30 :
    print ("Calificación: Sobrepeso")
else :
    print ("Calificación: Obesidad")
# ✅ Bien hecho: muy buen uso de los rangos encadenados (18.5 <= imc < 25). Y el round(imc, 2) suma legibilidad.

# 13.Conversión de unidades
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. 
# La fórmula de conversión es `F = C * 9/5 + 32`.
# Pide al usuario que ingrese una temperatura en Celsius y muestra el resultado en Fahrenheit.

temperaturaC = float (input ("Ingresá la tempratura en Celsius: "))
Fahrenheit = (temperaturaC * 1.8) + 32
print (f"La temperatura en Fahrenjeit es: {Fahrenheit}")
# ✅ Bien hecho: la fórmula está bien (1.8 = 9/5).
# 💡 Sugerencia: cuidado con los typos → "tempratura" → "temperatura"; "Fahrenjeit" → "Fahrenheit".

# 14.Juego de adivinanza
# Crea un programa que pida al usuario que adivine un número entre 1 y 10. 
# El programa debe comparar el número ingresado con uno predefinido (por ejemplo, 7) y 
# decir si es correcto o no. 
# Si es incorrecto, debe dar una pista si el número es mayor o menor.

numero_secreto = 5
intento = int (input ("Adivina el número entero entre el 1 y el 10: "))
if intento == numero_secreto :
    print ("GANASTE!!!!!")
elif intento < numero_secreto :
    print ("Incorrecto. El número secreto es mayor.")
else :
    print ("Incorrecto. El número secreto es menor.")


secreto = 6
intento = 0
while intento != secreto:
    intento = int(input("Adiviná el número secreto entre 1 y 10: "))
    if intento == secreto:
        print("¡Felicidades! ADIVINASTE EL NÚMERO.")
    elif intento < secreto:
        print("INCORRECTO. El número secreto es mayor")
    else:
        print("INCORRECTO. El número secreto es menor")
# ✅ Bien hecho: ¡plus! Hiciste una segunda versión del juego con un while que permite seguir intentando.
#                Esto ya está pisando temas de Unidad 4 (bucles), buen anticipo.

# 15.Identificación del tipo de dato


# Escribe un programa que tome una entrada del usuario usando input() y 
# determine qué tipo de dato representa la cadena ingresada. 
# Ten en cuenta que input() siempre devuelve una cadena de texto (string), 
# pero el usuario puede haber ingresado algo que representa un número.

# Tu programa debe analizar la entrada y determinar si representa:

#     Un número entero (positivo o negativo)
#     Un número flotante (positivo o negativo)
#     Una cadena de texto

# Requisitos específicos:

#     Usa el método isdigit() para verificar si todos los caracteres son dígitos
#     Para números negativos, verifica si el primer carácter es un guión (-) usando indexación
#     Para números flotantes, verifica si contiene exactamente un punto decimal
#     Imprime un mensaje claro indicando qué tipo de dato representa la entrada


# Ejemplo de salidas esperadas:

# Entrada: "123" → "El dato representa un número entero"
# Entrada: "-45" → "El dato representa un número entero negativo"
# Entrada: "3.14" → "El dato representa un número flotante"
# Entrada: "-2.5" → "El dato representa un número flotante"
# Entrada: "hola" → "El dato representa una cadena de texto"

dato = input("Ingresá un dato: ")
if "." in dato and dato.replace(".", "", 1).replace("-", "", 1).isdigit():
    print("El dato representa un número flotante")
elif dato.startswith("-") and dato[1:].isdigit():
    print("El dato representa un número entero negativo")
elif dato.isdigit():
    print("El dato dato representa un número entero")
else:
    print("El número representa una cadena de texto")
# ✅ Bien hecho: ejercicio difícil resuelto con sólido manejo de strings (replace, startswith, isdigit, indexación).
# 💡 Sugerencia: hay un typo "El dato dato representa..." (palabra "dato" repetida).
# 💡 Sugerencia: en el último else convendría decir "El dato representa..." (no "El número") porque
#                justamente ahí ya determinaste que NO es número.

# 16.Calculador de calificaciones
# Crea un programa que pida al usuario que ingrese sus calificaciones en tres materias. 
# Luego, calcula el promedio de esas calificaciones e imprime un mensaje que indique si 
# el alumno aprobó (promedio ≥ 6) o no.

nota1 = float (input ("Ingresá tu nota de la primera materia: "))
nota2 = float (input ("Ingresá tu nota de tu segunda materia: "))
nota3 = float (input ("Ingresá tu nota de tu tercera materia: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 6 :
    print ("APROBASTE")
else :
    print ("Desaprobado")
# ✅ Bien hecho: cálculo de promedio y comparación correctos.
# 💡 Sugerencia: estaría bueno mostrar el promedio antes del veredicto (print(f"Promedio: {promedio}")).

# 17.Concatenación de strings
# Escribe un programa que pida al usuario su nombre y su color favorito. 
# Luego, concatena estos datos en una sola oración que diga
#  "Hola [nombre], tu color favorito es [color]" y la imprima.

nombre = input ("Ingresá tu nombre: ")
color = input ("Insgresá tu color favorito: ")
print (f"Hola {nombre}!, tu color favorito es {color}")
# ✅ Bien hecho: f-string limpio y prolijo.
# 💡 Sugerencia: typo → "Insgresá" debería ser "Ingresá".