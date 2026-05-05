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


"""
EJERCICIO 3 — Eliminar Duplicados de una Lista
################################################

Escribí una función llamada `eliminar_duplicados(lista)` que reciba una lista
y devuelva una nueva lista con los mismos elementos pero sin repetidos.
El orden de aparición de los elementos debe mantenerse (se conserva la primera vez
que aparece cada elemento).

Importante: no uses `set()` para resolver esto.
Debés recorrer la lista con un bucle y verificar manualmente si el elemento ya fue agregado.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista1 = [1, 2, 3, 1, 2, 4]
    # Resultado esperado: [1, 2, 3, 4]

    lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
    # Resultado esperado: ["Pedro", "Florencia", "Ana"]

    lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
    # Resultado esperado: [1, 2, 3, 4, "Pedro", "Florencia", "Ana"]

"""
def eliminar_duplicados(lista) :
    lista_limpia = []
    for elemento in lista :
        if elemento not in lista_limpia :
            lista_limpia.append(elemento)
    return lista_limpia
lista1 = [1, 2, 3, 1, 2, 4]
print (f"Resultado 1: {eliminar_duplicados(lista1)}")
lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
print (f"Resultado 2: {eliminar_duplicados(lista2)}")
lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
print (f"Resultado 3: {eliminar_duplicados(lista3)}")

"""
EJERCICIO 4 — Contar Apariciones en una Lista
###############################################

Escribí una función llamada `contar_apariciones(lista, elemento)` que reciba
una lista y un elemento, y devuelva cuántas veces aparece ese elemento en la lista.

Importante: no uses el método `.count()` de las listas.
Debés recorrer la lista con un bucle y contar manualmente.

Luego escribí otra función llamada `contar_todos(lista)` que reciba una lista
y devuelva un resumen de cuántas veces aparece cada elemento único.
El resultado debe imprimirse de esta forma (un elemento por línea):

    "manzana" aparece 3 veces
    "pera" aparece 1 vez
    "naranja" aparece 2 veces

Probá las funciones con los siguientes ejemplos:

    frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

    print(contar_apariciones(frutas, "manzana"))  # 3
    print(contar_apariciones(frutas, "pera"))     # 1
    print(contar_apariciones(frutas, "uva"))      # 0

    contar_todos(frutas)
    # manzana aparece 3 veces
    # pera aparece 1 vez
    # naranja aparece 2 veces

Nota: para `contar_todos` podés apoyarte en la función `eliminar_duplicados`
del ejercicio anterior, o resolverlo de otra manera.

"""
def contar_apariciones(lista, elemento_a_buscar) :
    contador = 0
    for item in lista :
        if item == elemento_a_buscar :
            contador = contador + 1 
    return contador

def contar_todos(lista) :
    unicos = []
    for item in lista :
        if item not in unicos :
            unicos.append(item)
    for item in unicos :
        cantidad = contar_apariciones(lista, item)
        print (f"'{item}' aparece {cantidad} veces")
frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]
print (f"Manzanas detectadas: {contar_apariciones(frutas, 'manzana')}")
print (f"Uvas detectadas: {contar_apariciones(frutas, 'uva')}")
print ("---Resumen Completo---")
contar_todos(frutas)
