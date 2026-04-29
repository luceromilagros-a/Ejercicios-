"""
Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo es Pi (aproximadamente 3,141592) por el radio al cuadrado.

Nota: Utilice como valor de pi el valor 3.141592.

"""



print("T- Calcular el área de un triángulo")
print("C- Calcular el área de un círculo")

opcion = input("Ingrese la opción (T/t para triángulo, C/c para círculo): ")

if opcion.lower() == 't':
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = (base * altura) / 2
    print(f"El área del triángulo es: {area_triangulo}")

elif opcion.lower() == 'c':
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo = 3.141592 * (radio ** 2)
    print(f"El área del círculo es: {area_circulo}")

else:
    print("Opción no válida. Por favor, ingrese T/t para triángulo o C/c para círculo.")


