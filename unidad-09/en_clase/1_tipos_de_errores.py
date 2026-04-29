

numero = input("Ingresa un numero: ")


try:
    numero / numero
except Exception as e:
    print(e)


# Para Windows:
# >>> mi_entorno\Scripts\activate.bat
# Después de activarlo, verás algo así en la terminal:
# >>> (mi_entorno) C:\Usuarios\tu_usuario>






    print(f"El número reciproco de {numero} es {1/numero}")

except ValueError:
    pass

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except:
    print("Error inesperado......", e)

else:
    # El bloque else se ejecuta si no hubo excepciones en el bloque try
    print("Estoy dentro del bloque else")

finally:
    print("Estoy dentro del bloque finally")





# Es importante tener buenas prácticas en el manejo de las excepciones como las siguientes:



# Evitar bloques except: sin tipo de excepción. except:	print("Ocurrió un error")

# Capturar excepciones específicas en lugar de genéricas.
# Genérica -> except Exception as e:
# Especifica -> except FileNotFoundError:

# Usar finally para limpieza de recursos. El bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no. Es ideal para cerrar archivos, conexiones a bases de datos o sockets.

# Registrar errores (logging) en lugar de solo imprimir. Es un módulo para generación de logs.

# No abusar de los bloques try-except (anti-patrón "Swallowing Exceptions"). Se refiere a la práctica de capturar una excepción sin hacer nada significativo con ella , como simplemente ignorarla o silenciarla con un pass, print() vacío o un mensaje genérico que no ayuda a diagnosticar el error.


print("fin del programa")




exit()





print("El resultado es:", total)




exit()




# Error de sintaxis (SyntaxError)
# Descomenta la línea siguiente para ver el error:
# print("Hola mundo"  # Falta el paréntesis de cierre → SyntaxError

# Error semántico o lógico (no muestra error, pero el resultado es incorrecto)
def dividir(a, b):
    return a / (b - b)  # Lógica incorrecta: siempre divide entre 0

# Resultado inesperado (error lógico)
try:
    # aca empieza el bloque try
    print(dividir(10, 5))  # Esto dará ZeroDivisionError
except ZeroDivisionError as e:
    print("Error lógico causó una excepción:", e)

# Error en tiempo de ejecución (excepción)
try:
    numero = int("hola")  # ValueError
except ValueError as e:
    print("Error de conversión:", e)
