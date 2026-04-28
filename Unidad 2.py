# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.

print ("El área de un rectángulo con base 5 y altura 3 es: " , 5 * 3)

# 2. Convierte la temperatura de Celsius a Fahrenheit. 
# Pide al usuario ingresar la temperatura en Celsius y luego 
# imprime la temperatura equivalente en Fahrenheit.

celsius = float (input("Ingresá la temperatura en Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print (f"La termperatura en Fahrenheit es: {fahrenheit}")

# 3. Concatena tu nombre y tu edad como strings y 
# guárdalos en una variable. Luego imprime el tipo de dato de esa variable.

nombre = input ("¿Cúal es tu nombre?: ")
edad = input ("¿Cúantos años tenes?: ")
resultado = f"Mi nombre es: {nombre} y tengo {edad} años"
print (resultado)
print (type (resultado))

# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.

radio = 4
area = 3.14 * (radio ** 2)
print (f"El área de un circulo con radio de 4 es de : {area}")

# 5. Pide al usuario que ingrese dos números y muestra la suma, 
# resta, multiplicación y división de esos números.

n1 = float (input ("Ingresá el primer número: "))
n2 = float (input ("Ingresá el segundo número: "))

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

print (f"Resultados:\n" \
       f"- Suma: {suma}\n" \
       f"- Resta: {resta}\n" \
       f"- Multiplicación: {multiplicacion}\n" \
       f"- División: {division} ")

# 6. Almacena el resultado de una operación aritmética compleja en 
# una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.

resultado = (n1 * n2) / n1 + n2 #Use las mismas variables 
                                #de antes para no tener que volver a ponerlas
print (f"El resultado de la operción es: {resultado}")
print (f"El tipo de resulrado de dato es: {type(resultado)}")

# 7. Crea una variable booleana que represente si un alumno ha 
# aprobado o no un examen y luego imprime su estado.

nota = float (input ("Ingresá tu nota de exámen: "))
aprobado = nota >= 6 
if aprobado:
    print ("Felicidades APROBASTE!!!!!")
else:
    print ("No aprobado, seguí intentando nos vemos en el recu")

# 8. Calcula el perímetro de un triángulo equilátero con lados 
# de longitud 6. Imprime el resultado.

lado = 6 
perimetro = lado * 3
print (f"El perímetro de un triángulo con lados de 6cm es: {perimetro}")

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de 
# residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.

nombre = input ("Ingresá tu nombre: ")
edad = int (input ("Ingresá tu edad:"))
ciudad = input ("Ingresá tu ciudad: ")
print (f"El tipo de datos de estas variables es:\n" \
       f"Nombre {type(nombre)}\n" \
       f"Edad: {type(edad)}\n" \
       f"Ciudad: {type(ciudad)}")

# 10. Realiza una operación matemática que involucre paréntesis, 
# multiplicación, suma y resta. Guarda el resultado en una variable y 
# luego imprímela junto con su tipo de dato.

Resultado = (20 - 3) * 5 - 30 * (6 * 0)
print (f"El resultado de la operación es : {Resultado}")
print (f"El tipo de dato de la variable es: {type(Resultado)}")

