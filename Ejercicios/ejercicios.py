
# #UNIDAD 4#

# """

# 1. Solicita al usuario que ingrese su nombre y su edad. Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".

# 2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

# +***************+
# *               *
# *               *
# *               *
# +***************+

# +---+
# |   |
# |   |
# |   |
# +---+

# ###################################
# ###################################
# ##                               ##
# ##                               ##
# ##                               ##
# ###################################
# ###################################



# 3. Solicita al usuario que ingrese dos números enteros. Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.


# 4. Pide al usuario que ingrese una cadena que represente un número entero. Convierte esta cadena a un entero usando la función int() y luego suma 10. Imprime el resultado.


# 5. Pregunta al usuario que ingrese un número. Si el número es mayor que 10, imprime "El número es mayor que 10". Si es igual a 10, imprime "El número es igual a 10". De lo contrario, imprime "El número es menor que 10".


# 6. Solicita al usuario que ingrese dos números y compara si son iguales. Si lo son, imprime "Los números son iguales". De lo contrario, imprime "Los números son diferentes".


# 7. Pregunta al usuario que ingrese su edad. Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". De lo contrario, imprime "Eres menor de edad".


# 8. Pide al usuario que ingrese una temperatura en Celsius. Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". Si es menor o igual a 0, imprime "El agua está congelada". De lo contrario, imprime "El agua está en estado líquido".


# 9. Pregunta al usuario que ingrese un número. Si es positivo, imprime "El número es positivo". Si es negativo, imprime "El número es negativo". Si es cero, imprime "El número es cero".


# 10. Solicita al usuario que ingrese un número del 1 al 7. Luego, imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si ingresa un número fuera de ese rango, imprime "Número de día no válido".


# 11.Calculadora básica
# Crea un programa que tome dos números como entrada y luego imprima la suma, resta, multiplicación y división de esos dos números. Usa operadores aritméticos y asegúrate de manejar casos donde el divisor sea cero.


# 12.Calculador de IMC
# Crea un programa que calcule el Índice de Masa Corporal (IMC) de una persona. Pide al usuario su peso en kilogramos y su altura en metros. Luego, calcula el IMC usando la fórmula `IMC = peso / altura**2` y muestra el resultado con un mensaje que indique si el IMC está en el rango normal, bajo peso, sobrepeso, etc.


# 13.Conversión de unidades
# Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es `F = C * 9/5 + 32`. Pide al usuario que ingrese una temperatura en Celsius y muestra el resultado en Fahrenheit.


# 14.Juego de adivinanza
# Crea un programa que pida al usuario que adivine un número entre 1 y 10. El programa debe comparar el número ingresado con uno predefinido (por ejemplo, 7) y decir si es correcto o no. Si es incorrecto, debe dar una pista si el número es mayor o menor.


# 15.Identificación del tipo de dato


# Escribe un programa que tome una entrada del usuario usando input() y determine qué tipo de dato representa la cadena ingresada. Ten en cuenta que input() siempre devuelve una cadena de texto (string), pero el usuario puede haber ingresado algo que representa un número.

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






# 16.Calculador de calificaciones
# Crea un programa que pida al usuario que ingrese sus calificaciones en tres materias. Luego, calcula el promedio de esas calificaciones e imprime un mensaje que indique si el alumno aprobó (promedio ≥ 6) o no.


# 17.Concatenación de strings
# Escribe un programa que pida al usuario su nombre y su color favorito. Luego, concatena estos datos en una sola oración que diga "Hola [nombre], tu color favorito es [color]" y la imprima.



# """
# # 1 #

# nombre = input ("Por favor, ingresá tu nombre: ")
# edad = input ("Por favor, ingresá tu edad: ")
# print (f"¡Hola, {nombre}! Tienes {edad} años.")

# # 2 #

# lado_a = "+" + ("*" * 15) + "+"
# lado_b = "*" + (" " * 15) + "*"
# print (lado_a)
# print (lado_b)
# print (lado_b)
# print (lado_b)
# print (lado_a)

# print ("\n") 

# lado_c = "+" + ("-" * 3) + "+"
# lado_d = "|" + (" " * 3) + "|"
# print (lado_c)
# print (lado_d)
# print (lado_d)
# print (lado_d)
# print (lado_c)

# print ("\n")

# lado_e = "#" * 35 
# lado_f = "##" + (" " * 31) + "##"
# print (lado_e)
# print (lado_e)
# print (lado_f)
# print (lado_f)
# print (lado_f)
# print (lado_e)
# print (lado_e)

# # 3 #

# n1 = float (input("Ingresá un número entero: "))
# n2 = float (input("Ingresá otro número entero: "))

# resultado = n1 / n2 
# print(f"El resultado de dividir {n1} por {n2} es: { resultado } ") 

# # 4 #

# numero = int(input("Ingresá un número entero: "))
# resultado = numero + 10
# print (f"El número ingresado sumado a 10 es: { resultado }")

# # 5 #
# numero_i = input("Ingresá un número: ")
# numero = float(numero_i)

# if numero > 10:
#     print("El número es mayor que 10")
# elif numero == 10:
#     print("El número es igual a 10")
# else:
#     print("El número es menor que 10")

# # 6 #

# n1 = float(input("Ingresá el primer número: "))

# n2 = float(input("Ingresá el segundo número:"))

# if n1 == n2:
#     print("Los números son iguales")
# else:
#     print("Los números son diferentes")

# # 7 #

# edad = int(input("Ingresá tu edad: "))

# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print ("Eres menor de edad")

# # 8 #

# temperatura = float(input("Ingresá la temperatura en Celcius: "))
# if temperatura >= 100:
#     print("El agua está hirviendo")
# elif temperatura <= 0:
#     print("El agua está congelada")
# else:
#     print("El agua está líquida")

# # 9 #

# numero = float(input("Ingresá un número: "))
# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# else:
#     print("El número es cero")

# # 10 #

# dia = int(input("Ingresá un número del 1 al 7: "))

# if dia == 1:
#     print("Lunes")
# elif dia == 2:
#     print("Martes")
# elif dia == 3:
#     print("Miércoles")
# elif dia == 4:
#     print("Jueves")
# elif dia == 5:
#     print("Viernes")
# elif dia == 6:
#     print("Sábado")
# elif dia == 7:
#     print("Domingo")
# else:
#     print("Número de día no válido")

# # 11 #

# n1 = float(input("Ingresá el primer número: "))
# n2 = float(input("Ingresá el segundo número: "))

# suma = n1 + n2
# resta = n1 - n2
# multiplicacion = n1 * n2

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Multiplicación: {multiplicacion}")

# if n2 != 0:
#     division = n1 / n2
#     print(f"División: {division}")
# else:
#     print("División: Error (No se puede dividir por cero)")

# 12 #

# peso = float(input("Ingresá tu peso en kg: "))
# altura = float(input("Ingresá tu altura en cm: "))
# imc = peso / (altura ** 2)
# print(f"Tu IMC es : {imc: .2f}")

# if imc < 18.5:
#     print("Estado: Bajo peso")
# elif 18.5 <= imc < 25:
#     print("Estado: Sobrepeso")
# else:
#     print("Estado: Obesidad")
    
# 13 #    

# C = float(input("Ingresá la temperatura en Celsius: "))
# fahrenheit = (C * 9/5) + 32
# print (f"{C} °C equivale a {fahrenheit: .1f} °F")

# 14 #

# secreto = 6 
# intento = 0
# while intento != secreto:
#     intento = int(input("Adiviná el número secreto entre 1 y 10: "))
#     if intento == secreto:  
#         print("¡Felicidades! ADIVINASTE EL NÚMERO.")
#     elif intento < secreto:
#         print("INCORRECTO. El número secreto es mayor")
#     else:
#         print("INCORRECTO. El número secreto es menor")

# 15 #

# dato = input("Ingresá un dato: ")
# if "." in dato and dato.replace(".", "", 1).replace("-", "", 1).isdigit():
#     print("El dato representa un número flotante")
# elif dato.startswith("-") and dato[1:].isdigit():
#     print("El dato representa un número entero negativo")
# elif dato.isdigit():
#     print("El dato dato representa un número entero")
# else:
#     print("El número representa una cadena de texto")

# 16 #

# nota1 = float(input("Ingresá tu nota de la materia 1: "))
# nota2 = float(input("Ingresá tu nota de la materia 2: "))
# nota3 = float(input("Ingresá tu nota de la materia número 3: "))
# promedio = (nota1 + nota2 + nota3) / 3 
# print(f"Tu promedio final es: {promedio: .2}")
# if promedio >= 6:
#     print("Estado: ¡APROBADO!")
# else: 
#     print("Estado: DESAPROBADO")

# 17 #

# nombre = input("Ingresá tu nombre: ")
# color = input("Ingresá tu color favorito: ")
# print(f"Hola {nombre}, tu color favorito es {color}")