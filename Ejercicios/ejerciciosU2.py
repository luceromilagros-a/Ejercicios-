# # 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.
int (5*3)
# ❌ Error: la consigna pide IMPRIMIR el resultado. Acá calculás 5*3 pero nunca lo mostrás.
# 💡 Sugerencia: usá print(5*3) o guardalo en una variable y luego print(area).
# 💡 Sugerencia: el int() acá es innecesario porque 5*3 ya es entero.

# # 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.

Celsius= input ("Decime la temperatura en celsius: ")
temperatura= float (Celsius)
Fahrenheit= (temperatura * 9/5) + 32
print ( Fahrenheit, "Fahrenheit")
# ✅ Bien hecho: la fórmula está correcta y la conversión a float también.
# 💡 Sugerencia: por convención (PEP 8), los nombres de variables se escriben en minúsculas (celsius, fahrenheit).
# 💡 Sugerencia: podés ahorrar la variable intermedia: temperatura = float(input("..."))


# # 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.

Nombre = input ("Decime tu nombre:")
Edad = input ("Decime tu edad:")
print ( "Nombre: ", Nombre, "Edad: ", Edad)
# ❌ Error: la consigna pide CONCATENAR nombre y edad en UNA variable e imprimir el TIPO de dato.
# 💡 Sugerencia: deberías hacer algo como:
#     datos = Nombre + " " + Edad
#     print(datos)
#     print(type(datos))

# # 4. Calcula el área de un círculo con radio 4. Imprime el resultado.

radio = 4
pi_manual = 3.14
area = pi_manual*(radio ** 2)
print ("El área es: ", area)
# ✅ Bien hecho: usás una constante para pi y aplicás bien la fórmula π·r².
# 💡 Sugerencia: para mayor precisión podrías importar `from math import pi`.

# # 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.

numero1 = float (input ("Decime un numero: "))
numero2 = float (input ("Decime otro numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2 
division = numero1 / numero2 
print ("Suma: " , suma , "resta: " , resta ,  "multiplicación: " , multiplicacion , "división: " , division)
# ✅ Bien hecho: convertís correctamente los inputs a float y aplicás las 4 operaciones.
# 💡 Sugerencia: tener en cuenta que si numero2 es 0, la división va a tirar error (ZeroDivisionError).
#                Más adelante en U3 ya lo manejás con un if, ¡buen avance!


# # 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.

resultado = (10 * 3)+ 20 / (10 ** 3) - 2

print ("El resultado de la operación es: " , resultado ) 

tipo_de_dato = type (resultado)

print ("El tipo de dato de la variable es: " , tipo_de_dato )
# ✅ Bien hecho: cumplís con la consigna mostrando resultado y type().


# # 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.

nota = 9
minimo_de_aprobacion = 4
aprobado = nota >= minimo_de_aprobacion
print ("El alumno esta aprobado?: " , nota )
# ❌ Error: estás imprimiendo `nota` en lugar de `aprobado`. La consigna pide imprimir el ESTADO booleano.
# 💡 Sugerencia: cambiar a print("El alumno está aprobado?: ", aprobado)  →  mostraría True / False.
if aprobado:
    print ("APROBASTE")

else:
    print ("DESAPROBADO")
# ✅ Bien hecho: la lógica del if/else está correcta y el booleano se calcula bien.


# # 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.

perimetro = 6*3
print ("El perímetro del triángulo es: " , perimetro )
# ✅ Bien hecho: corto y al punto.

# # 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.

nombre = input ("Ingresa tu nombre completo: ")

edad = int (input ("Ingresa tu edad: "))

ciudad_de_residencia = input ("Ingresa tu ciudad de residencia: ")

print ("---DATOS DEL USUARIO---")
print ("Nombre: " , nombre)
print ("Tipo de dato: " , type ( nombre ))
print ("Edad: " , edad)
print ("Tipo de dato: " , type ( edad ))
print ("Ciudad de residencia: " , ciudad_de_residencia )
print ("Tipo de dato: " , type ( ciudad_de_residencia ))
# ✅ Bien hecho: este ejercicio está completo. Pedís los 3 datos, los convertís cuando hace falta
#                (edad a int) y mostrás cada valor con su type(). Muy prolijo.




# # 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.

operacion = float (((3 * 5) + 20) - 2)
print ("Resultado: " , operacion )
print ("Tipo de dato: " , type (operacion) )
# ✅ Bien hecho: usás paréntesis para controlar el orden de las operaciones.
# 💡 Sugerencia: el float() acá es opcional. Sin él el resultado igual es un int válido.