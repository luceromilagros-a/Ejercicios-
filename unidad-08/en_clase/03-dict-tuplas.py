

# Ejemplo de uso de tuplas como claves en un diccionario



# Crear un diccionario donde la clave es una tupla (coordenada x, y)
mapa_ciudades = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles",
    (41.8781, -87.6298): "Chicago",
    (51.5074, -0.1278): "Londres",
    (48.8566, 2.3522): "París"
}

# Acceder al valor usando una tupla como clave
coordenada_buscar = (41.8781, -87.6298)
ciudad = mapa_ciudades.get(coordenada_buscar, "Ciudad no encontrada")

print(f"La ciudad en la coordenada {coordenada_buscar} es: {ciudad}")

