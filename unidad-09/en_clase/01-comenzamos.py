

try:
    numero = input("Ingrese un numero: ")
    numero = int(numero)
    print(f"El reciproco de {numero} es {1/numero}")

except ZeroDivisionError:
    print("No se puede dividir entre cer0")
except ValueError:
    print("El valor no es un numero")

except:
    print("error general")

finally:
    print("esto esta adentro de finally")



print("aca termina")
exit()



print("fin del programa")


exit()




# errores en tiempo de ejecucion


