##1. Solicita al usuario que ingrese su nombre y su edad. 
##Luego, imprime un mensaje que diga "¡Hola, [nombre]! Tienes [edad] años".

nombre = input ("Ingresá tu nombre: ")
edad = input ("Ingresá tu edad: ")
print (f"¡Hola, {nombre}! Tienes {edad} años")


## 2. Imprima en pantalla las siguientes figuras geometricas (utilizar concatenación y replicación de strings)

#  +***************+
#  *               *
#  *               *
#  *               *
#  +***************+

#  +---+
#  |   |
#  |   |
#  |   |
#  +---+

#  ###################################
#  ###################################
#  ##                               ##
#  ##                               ##
#  ##                               ##
#  ###################################
#  ################################### 

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


# 3. Solicita al usuario que ingrese dos números enteros. 
# Luego, convierte estos números a float, realiza la división de ambos y muestra el resultado.

nE1 = input ("Ingresá el primer número entero: ")
nE2 = input ("Ingresá el segundo número entero: ")
n1 = float (int (nE1))
n2 = float (int (nE2))
division = n1 / n2
print (f"El resultado de la división es: {division}")


# 4. Pide al usuario que ingrese una cadena que represente un número entero. 
# Convierte esta cadena a un entero usando la función int() y luego suma 10. 
# Imprime el resultado.

cadena = input ("Ingresá un número entero: ")
numero = int (cadena) + 10
print (f"El resultado de la suma es de: {numero}")