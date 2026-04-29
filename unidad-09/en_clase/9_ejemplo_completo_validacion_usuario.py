
# EJEMPLO INTEGRADOR: Validación de entrada del usuario

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        break
    except ValueError as ve:
        print("Error:", ve)
        print("Por favor, ingrese un número válido.")

print(f"Edad ingresada: {edad}")
