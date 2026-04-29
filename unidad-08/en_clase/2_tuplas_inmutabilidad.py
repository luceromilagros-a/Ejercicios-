
# LAS TUPLAS SON INMUTABLES
tupla = (1, 2, 3)

tupla[0] = 100  # Esto genera un error

# PERO SE PUEDEN REASIGNAR COMO OBJETO ENTERO
tupla = (100, 2, 3)
print("Nueva tupla:", tupla)
