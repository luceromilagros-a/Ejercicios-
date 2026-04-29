range(10)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


for numero in range(10):
    if numero % 2 != 0:  # es numero PAR
        continue
    print("Aca seguimos....")
    print(numero)
    print("-------------------")
else:
    print("entra al final una sola vez....")


print("Fin del programa")

exit()


# for

# ahora vamos a ver for
for numero_entero in range(10, 21, 2):
    print("Valor del numero: ", numero_entero)


exit()


muchos_nombres = [
    "Juan",
    "Pedro",
    "María",
    "Ana",
    "Luis",
    "Carlos",
    "Sofía",
    "Laura",
    "Javier",
    "Lucía",
    "Diego",
    "Valeria",
    "Andrés",
    "Natalia",
    "Fernando",
    "Gabriela",
    "Ricardo",
    "Patricia",
    "Alejandro",
    "Isabel",
    "Santiago",
]

# for <mivariables> in <todosloselementos>:
#     <bloque de instrucciones>
#       imprimiendo cada elemenot
#     print("El nombre es: " + mivariable)
# for nombre in muchos_nombres:

for nombre in muchos_nombres:
    # acá empieza el bloque de codigo dentro del for()
    print(nombre)
    # aca termina el bloque de codigo dentro del for()

print("Fin del programa")
exit()


# extendiendo un poco el uso de range()

for i in range(2, 17, 3):
    print("El valor de la variable i es: " + str(i))
