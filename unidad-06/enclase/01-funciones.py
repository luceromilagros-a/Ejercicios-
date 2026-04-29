



def sumar( *numeros ):
    """
    Esta función recibe cuatro números y retorna la suma de ellos
    """
    subtotal = 0
    
    for num in numeros:
        subtotal = subtotal + num

    return subtotal


def saludar():
    return "Hola como estas"




print(sumar(4, 5, 20, 40, 100))


exit()




print(saludar())


exit()
























saludar()


print("Acá termina mi programa.")

exit()

























def sumar_numeros( numero_uno = 0, numero_dos = 0, numero_tres = 0):
    total = numero_uno + numero_dos + numero_tres
    return total


def raiz_cuadrada( numero = 0):
    raiz_cuadrada = numero ** 0.5
    return raiz_cuadrada



sumo_numeros = sumar_numeros(10,10,5)

subtotal = raiz_cuadrada(sumo_numeros)

print(subtotal)



























def miprimerfuncion():
    print( "Hola Mundo" )
    pass



# docstring sirve para documentar la función
def sumar_dos_numeros( nro_uno = 0, nro_dos = 0):
    """
    Esta función recibe dos números y retorna la suma de ellos
    param nro_uno: int
    param nro_dos: int
    return: int
    """
    if nro_dos == 0:
        print( "No se ha ingresado el segundo número" )
        return "Error"
    # inicio del blque de la función
    total = nro_uno + nro_dos
    return total















