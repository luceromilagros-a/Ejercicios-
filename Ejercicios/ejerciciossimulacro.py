"""
EJERCICIO 1 — Validar Contraseña
##################################

Escribí una función llamada `validar_contrasena(contrasena)` que reciba un string
y retorne `True` si la contraseña es válida, o `False` si no lo es.

Condiciones que debe cumplir una contraseña válida:

1. Debe tener al menos 8 caracteres.
2. Debe contener al menos una letra mayúscula (A-Z).
3. Debe contener al menos una letra minúscula (a-z).
4. Debe contener al menos un dígito (0-9).
5. No debe contener espacios en blanco.

No uses expresiones regulares (módulo `re`). Recorré el string con un bucle
y verificá cada condición manualmente.

Ejemplos:

    validar_contrasena("Hola1234")      # True
    validar_contrasena("hola1234")      # False  (sin mayúscula)
    validar_contrasena("HOLA1234")      # False  (sin minúscula)
    validar_contrasena("HolaMundo")     # False  (sin dígito)
    validar_contrasena("Hola 123")      # False  (tiene espacio)
    validar_contrasena("Ho1")           # False  (menos de 8 caracteres)

Ayuda: podés usar los métodos `.isupper()`, `.islower()` y `.isdigit()` para
verificar el tipo de cada carácter dentro del bucle.

"""
def validar_contrasena(contrasena) :
    if len (contrasena) < 8 :
        return False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    for caracter in contrasena :
        if caracter == " " :
            return False
        if caracter.isupper() :
            tiene_mayuscula = True
        if caracter.islower() :
            tiene_minuscula = True
        if caracter.isdigit() :
            tiene_digito = True
    if tiene_mayuscula and tiene_minuscula and tiene_digito :
        return True
    else: 
        return False

print(validar_contrasena("Hola1234"))      
print(validar_contrasena("hola1234"))      
print(validar_contrasena("HOLA 123"))

"""
EJERCICIO 2 — Combinar Dos Listas
##################################

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas
como parámetros y devuelva una nueva lista con todos los elementos de ambas,
primero los de `lista1` y luego los de `lista2`.

Importante: no uses el operador `+` entre listas ni el método `.extend()`.
Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    # Resultado esperado: [1, 2, 3, 4, 5, 6]

    lista_c = ["manzana", "pera"]
    lista_d = ["naranja", "uva", "durazno"]
    # Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]

"""
def combinar_listas(lista1,lista2) :
    lista_combinada = []
    for elemento in lista1 :
        lista_combinada.append(elemento)
    for elemento in lista2 :
        lista_combinada.append(elemento)
    return lista_combinada 
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
resultado1 = combinar_listas(lista_a, lista_b)
print (f"Resultado 1: {resultado1}")

lista_c = ["manzana", "pera"]
lista_d = ["naranja", "uva", "durazno"]
resultado2 = combinar_listas(lista_c, lista_d)
print (f"Resultado 2: {resultado2}")
