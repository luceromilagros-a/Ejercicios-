
# EXCEPCIONES ESPECÍFICAS

try:
    numero = int("abc")  # ValueError
except ValueError as ve:
    print("ValueError:", ve)

try:
    resultado = "texto" + 5  # TypeError
except TypeError as te:
    print("TypeError:", te)

try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
except IndexError as ie:
    print("IndexError:", ie)

try:
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()  # FileNotFoundError
except FileNotFoundError as fe:
    print("FileNotFoundError:", fe)
