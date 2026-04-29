
# MEZCLANDO TUPLAS Y DICCIONARIOS
empleados = {
    (1001, "juan"): {"nombre": "Juan", "salario": 3000, "departamento": "TI"},
    (1002, "ana"): {"nombre": "Ana", "salario": 3500, "departamento": "Ventas"}
}

# ACCEDER AL EMPLEADO POR CLAVE COMPUESTA (TUPLA)
clave = (1001, "juan")
print(f"Datos del empleado {clave}:\n{empleados[clave]}")

# ITERAR SOBRE EMPLEADOS
print("\nInformación de empleados:")
for (id_empleado, usuario), datos in empleados.items():
    print(f"ID: {id_empleado}, Usuario: {usuario}")
    print(f"Nombre: {datos['nombre']}, Salario: {datos['salario']}, Departamento: {datos['departamento']}")
    print("-" * 40)
