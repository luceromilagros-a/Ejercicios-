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
