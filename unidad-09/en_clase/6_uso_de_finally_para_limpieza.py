
# USO DE finally PARA RECURSOS (ejemplo con archivos)

try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    try:
        archivo.close()
        print("Archivo cerrado correctamente.")
    except NameError:
        print("No fue necesario cerrar el archivo.")
