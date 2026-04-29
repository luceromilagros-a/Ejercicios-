
# USO COMPLETO: try, except, else, finally

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Fin del intento de división.")

# Ejemplos de uso
dividir(10, 2)  # Caso exitoso
dividir(5, 0)    # Caso con excepción
