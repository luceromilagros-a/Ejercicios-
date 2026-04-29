
# BLOQUE try-exCEPT BÁSICO

numero = input("Ingresa un número: ")

try:
    numero = float(numero)
    print(f"El recíproco de {numero} es {1/numero}")
except ValueError:
    print("ERROR: El valor ingresado no es un número.")
    exit()
except ZeroDivisionError:
    print("ERROR: No se puede dividir por cero.")
print("Este mensaje se ejecuta después del bloque try-except")
