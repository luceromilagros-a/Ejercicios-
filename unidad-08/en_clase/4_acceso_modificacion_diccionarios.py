



nro_telefono = {
    'juan': 123456,
    'pedro': 987654,
}
print("Numero de telefono original")
print(nro_telefono)



# ACCESO A VALORES
print("Teléfono de Juan:", nro_telefono['juan'])
print(f"Teléfono de Pedro:", nro_telefono['pedro'])

# VERIFICAR EXISTENCIA DE CLAVE
if 'maria' in nro_telefono:
    print("María si tiene numero.")
    print("Teléfono de María:", nro_telefono['maria'])


# MODIFICAR VALOR
nro_telefono['pedro'] = 876876876
print("Nuevo teléfono de Pedro:", nro_telefono['pedro'])

# AGREGAR NUEVA CLAVE-VALOR
nro_telefono['ana'] = 333444
print("Después de agregar Ana:", nro_telefono)

print(nro_telefono)


# ELIMINAR CLAVE-VALOR
# nro_telefono['pedro'] = ""
del nro_telefono['pedro']


print("Después de eliminar Pedro:", nro_telefono)
