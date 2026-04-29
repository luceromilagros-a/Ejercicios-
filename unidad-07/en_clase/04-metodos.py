


# append() en listas

colores = ["rojo", "verde", "naranja", "gris", "violeta", "naranja"]
print(colores)

colores.append("azul")
print(colores)


# remove() en listas

colores.remove("naranja")
print(colores)


# pop() en listas
# Va a eliminar el ultimo elemento de la lista

colores.pop()
print(colores)
print(f" vamos a eliminar el elemento en la posicion 2: {colores.pop(2)}")
print(colores)

# metodo index()
# lo que va a devolver es la posicion del elemento que le pasemos como parametro

print(colores)

colores.append("verde")

print(colores)

print(f"La cantidad de veces que se repite verde es: {colores.count('verde')}")