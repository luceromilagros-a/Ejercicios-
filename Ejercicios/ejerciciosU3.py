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

# 5. Pregunta al usuario que ingrese un número. 
# Si el número es mayor que 10, imprime "El número es mayor que 10". 
# Si es igual a 10, imprime "El número es igual a 10". 
# De lo contrario, imprime "El número es menor que 10".

numero = int (input ("Ingresá un número: "))
if numero > 10:
    print ("El número es mayor a 10")
elif numero == 10:
    print ("El número es igual a 10")
else :
    print ("El número es menor que 10")
    
# 6. Solicita al usuario que ingrese dos números y compara si son iguales. 
# Si lo son, imprime "Los números son iguales". 
# De lo contrario, imprime "Los números son diferentes".

n1 = input ("Ingresá un número: ")
n2 = input ("Ingresá el segundo número: ")
if n1 == n2:
    print ("Los números son iguales")
else :
    print ("Los número son diferentes")

# 7. Pregunta al usuario que ingrese su edad. 
# Si la edad es mayor o igual a 18, imprime "Eres mayor de edad". 
# De lo contrario, imprime "Eres menor de edad".

edad = int (input ("Ingresá tu edad: "))
if edad >= 18 :
    print ("Eres mayor de edad")
else :
    print ("Eres menor de edad") 

# 8. Pide al usuario que ingrese una temperatura en Celsius. 
# Si la temperatura es mayor o igual a 100, imprime "El agua está hirviendo". 
# Si es menor o igual a 0, imprime "El agua está congelada". 
# De lo contrario, imprime "El agua está en estado líquido".

temperaturaC = float (input ("Ingresá la temperatura en Celsius: "))
if temperaturaC >= 100 :
    print ("El agua está hirviendo")
elif temperaturaC <= 0 :
    print ("El agua está congelada")
else :
    print ("El agua está en estado líquido")

