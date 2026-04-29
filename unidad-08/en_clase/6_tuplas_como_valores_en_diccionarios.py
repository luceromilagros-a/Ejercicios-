

agenda = {
    27656588: {
        "nombre": "Juan Pérez",
        "telefono": 123456789,
        "email": "jjd@djd.com"
    },
    12345678: {
        "nombre": "Ana Gómez",
        "telefono": 987654321,
        "email": "pepe@mail.com"
    },
    87654321: {
        "nombre": "Pedro López",
        "telefono": 456789123,
        "email": "jua@ma"
    }
}

print(agenda[27656588]["nombre"])

exit()

# DICCIONARIOS CON TUPLAS COMO VALORES
coordenadas_paises = {
    "Argentina": (-34.6037, -58.3816),
    "Brasil": (-15.7801, -47.9292),
    "Chile": (-33.4489, -70.6693),
    "Perú": (-12.0464, -77.0428)
}

# ACCEDER A COORDENADAS
pais = "Brasil"
latitud, longitud = coordenadas_paises[pais]
print(f"Las coordenadas de {pais} son: Latitud {latitud}, Longitud {longitud}")

exit()



# ITERAR SOBRE TODOS LOS PAÍSES
print("\nCoordenadas de todos los países:")
for pais, coordenadas in coordenadas_paises.items():
    print(f"{pais}: Latitud {coordenadas[0]}, Longitud {coordenadas[1]}")
