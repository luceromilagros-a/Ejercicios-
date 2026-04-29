
"""
Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x² + b x + c = 0) y escriba la solución.

Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única, tener dos soluciones o que todos los números sean solución. Se recuerda que la fórmula de las soluciones cuando hay dos soluciones es x = (-b ± √(b2-4ac) ) / (2a)

Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué corresponder con el orden de las condiciones).



a	b	c	Solución
1	-2	2	Sin solución real
2	-7	3	Dos soluciones: 0.5 y 3.0
1	2	1	Una solución: -1.0
0	0	5	Sin solución
0	0	0	Todos los números son solución
0	3	2	Una solución: -0.666...


"""




coeficiente_a = float(input("Ingrese el coeficiente a: "))
coeficiente_b = float(input("Ingrese el coeficiente b: "))
coeficiente_c = float(input("Ingrese el coeficiente c: "))

if coeficiente_a == 0 and coeficiente_b == 0 and coeficiente_c == 0:
    print("Todos los números son solución.")
elif coeficiente_a == 0 and coeficiente_b == 0:
    print("Sin solución.")
elif coeficiente_a == 0:
    solucion = -coeficiente_c / coeficiente_b
    print(f"Una solución: {solucion}")

else:
    discriminante = coeficiente_b**2 - 4 * coeficiente_a * coeficiente_c
    if discriminante < 0:
        print("Sin solución real.")
    elif discriminante == 0:
        solucion = -coeficiente_b / (2 * coeficiente_a)
        print(f"Una solución: {solucion}")
    else:
        solucion1 = (-coeficiente_b + discriminante**0.5) / (2 * coeficiente_a)
        solucion2 = (-coeficiente_b - discriminante**0.5) / (2 * coeficiente_a)
        print(f"Dos soluciones: {solucion1} y {solucion2}")

