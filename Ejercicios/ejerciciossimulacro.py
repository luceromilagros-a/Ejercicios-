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


"""
EJERCICIO 5 — Número Primo
###########################

Escribí una función llamada `es_primo(numero)` que reciba un número entero
y retorne `True` si es primo, o `False` si no lo es.

Un número es primo si es mayor a 1 y solo es divisible por 1 y por sí mismo.

Requisitos:
- Usá un bucle `while` para verificar los divisores (no uses `for`).
- Empezá a verificar desde el 2 hasta el número anterior al que se recibe.
- En cuanto encontrés un divisor, retorná `False` inmediatamente.
- Si el bucle termina sin encontrar divisores, retorná `True`.
- Si el número es menor o igual a 1, retorná `False` directamente.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    print(es_primo(2))   # True
    print(es_primo(7))   # True
    print(es_primo(11))  # True
    print(es_primo(1))   # False
    print(es_primo(4))   # False
    print(es_primo(9))   # False
    print(es_primo(0))   # False

"""
def es_primo(numero) :
    if numero <= 1 :
        return False
    divisor = 2
    while divisor < numero :
        if numero % divisor == 0 :
            return False 
        divisor = divisor + 1
    return True
print (es_primo(2))
print (es_primo(7))
print (es_primo(11))
print (es_primo(1))
print (es_primo(4))
print (es_primo(9))
print (es_primo(0))

"""
EJERCICIO 6 — Conversor de Unidades con Módulo
################################################

Desarrollá un programa que convierta unidades de distancia y peso.

El programa debe mostrar un menú al usuario y permitirle elegir qué conversión
realizar. Debe seguir mostrando el menú hasta que el usuario elija salir.

Menú:
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir

Fórmulas:
    - 1 kilómetro = 0.621371 millas
    - 1 kilogramo = 2.20462 libras

Requisitos:
- Las funciones de conversión deben estar en un módulo separado llamado `conversiones.py`.
- Cada función debe tener un docstring de una línea que explique qué hace.
  Ver formato: https://peps.python.org/pep-0257/#one-line-docstrings
- El menú y la lógica principal deben estar en este archivo (ejercicio_06.py).
- Si el usuario ingresa una opción inválida, mostrar "Opción no válida. Intente nuevamente."
- Validar que el valor ingresado para convertir sea un número positivo.

Ejemplo de ejecución:

    ¿Qué desea convertir?
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir
    Ingrese una opción: 1
    Ingrese los kilómetros: 10
    10 km = 6.21 millas

    Ingrese una opción: 2
    Ingrese los kilogramos: 70
    70 kg = 154.32 libras

    Ingrese una opción: 3
    ¡Hasta luego!

Mostrá los resultados redondeados a 2 decimales (por ejemplo, `f"{valor:.2f}"`).

"""
import conversiones 
def mostrar_menu() :
    print("\n---Menú de Conversiones ---")
    print ("1. Kilómetros a Millas")
    print ("2.Kilogramos a Libras")
    print ("3. Salir")
while True :
    mostrar_menu ()
    opcion = input ("Ingrese una opción: ")
    if opcion == "3" :
        print ("¡Hasta luego!")
        break
    if opcion == "1" or opcion == "2" :
        valor = float (input ("Ingrese la cantidad a convertir: "))
        if valor < 0 :
            print ("Error: El valor debe ser un número positivo.")
            continue
        if opcion == "1" :
            resultado = conversiones.km_a_millas(valor)
            print (f"{valor} km = {resultado:.2f} millas")
        else :
            resultado = conversiones.kg_a_libras(valor)
            print (f"{valor} kg = {resultado:.2f} libras")
    else :
        print ("Opción no válida. Intente nuevamente.")