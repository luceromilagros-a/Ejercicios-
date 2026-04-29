
nombre = "Juan"

# print(nombre[0])




# TUPLAS

coord_x = 1.76633
coord_y = 3.4545
coordenadas = (coord_x, coord_y)

nombres = ("Juan Pedro", "pepe", "juan")


nombres = tuple("Juan", "Pedro", "pepejuan")

lista_nombres_buscar = tuple(lista_nombres)


nombres_lista = list(lista_nombres_buscar)



if "pepe" in lista_nombres_buscar:
    print("Está pepe")
else:
    print("No está pepe")



exit()


# coord_x = 20.25
# coord_y = 20.44

# print(coordenadas)


exit()



for numero in numeros:
    print(numero)



exit()









# CREACIÓN DE TUPLAS
tupla_ejemplo = (10, "Python", True)
otra_tupla = (4, 5, 6)

print("Tupla ejemplo:", tupla_ejemplo)
print("Otra tupla:", otra_tupla)

# ACCESO A ELEMENTOS
colores = ("rojo", "verde", "azul")
print(f'Primer color: {colores[0].upper()}')



# ITERAR SOBRE UNA TUPLA
for color in colores:
    print(color.upper())

# USO DE len(), + Y *
print("Longitud de colores:", len(colores))
print("Unión de tuplas:", tupla_ejemplo + otra_tupla)
print("Multiplicar tupla:", colores * 2)

# OPERADORES IN / NOT IN
print("'rojo' en colores:", 'rojo' in colores)
print("'amarillo' not in colores:", 'amarillo' not in colores)
