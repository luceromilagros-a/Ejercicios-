


persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Buenos Aires"
}

# MÉTODO keys() -> recorro las claves
# print("Claves del diccionario:")
# for clave in persona.keys():
#     print(clave)

# # MÉTODO values() -> recorro los valores
# print("\nValores del diccionario:")
# for valor in persona.values():
#     print(valor)

# # MÉTODO items()
print("\nPares clave-valor:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
