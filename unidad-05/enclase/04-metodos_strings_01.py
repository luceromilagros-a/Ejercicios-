cadena_total = "milanesas"

len_cadena_total = len(cadena_total)

numero_decimal = 23.34

cantidad_s = numero_decimal

print(cantidad_s)

exit()


# Uso de index() -> nos va a devolver el indice de la primera ocurrencia de la subcadena que le pasamos como argumento

cadena = "Python es un lenguaje de alto nivel"

print(cadena[0:10])

numero = 30

indice = cadena

print(f"El indice de la palabra 'h' es: {indice}")

exit()


# #########################################################


# # Vamos a probar las diferentes maneras de ver los indices de una cadena


# cadena = "Python es un lenguaje de alto nivel"

# print(cadena[13:16])
# # salida: P

# exit()

# print(cadena[0:10])
# # salida: Python es

# print(cadena[10:20])
# # salida: un lenguaj

# print(cadena[0:20:2])
# # salida: Pto su ega

# cadena = "Python es un lenguaje de alto nivel"
# print(cadena[:-2])
# # salida: Python es un lenguaje de alto nive

# print(cadena[-1])
# # salida: l


# #########################################################


# # in y not in -> nos va a devolver True si la subcadena que le pasamos como argumento está en la cadena, False en caso contrario

numero_uno = input("Ingrese un número: ")

if numero_uno.isdigit():
    print("El string ingresado es un número")
else:
    print("El string ingresado no es un número")


print("Fin del programa")
