
## 🧪 Ejercicios Simples: Tratamiento de Errores y Excepciones

### ✅ Ejercicio 1: Capturar un `ValueError`
Escribe un programa que pida al usuario que ingrese un número entero. Si el usuario no ingresa un número válido, muestra un mensaje de error y vuelve a pedirlo.

💡 Pista: Usa un bucle `while` con `try-except`.

---

### ✅ Ejercicio 2: División segura
Crea un programa que:
- Pida dos números al usuario.
- Intente dividir el primero entre el segundo.
- Maneje los errores:
  - Si se ingresa texto en vez de número → `ValueError`.
  - Si el segundo número es cero → `ZeroDivisionError`.

Muestra mensajes claros para cada tipo de error.

---

### ✅ Ejercicio 3: Acceso seguro a listas
Dada la lista:

```python
numeros = [10, 20, 30]
```

Pide al usuario que ingrese un índice. Usa `try-except` para manejar el caso en que el índice esté fuera de rango (`IndexError`). Muestra un mensaje amigable si ocurre ese error.

---

### ✅ Ejercicio 4: Usar `else` y `finally`
Modifica el ejercicio anterior para que:
- En el bloque `else`, muestre el valor del índice si fue correcto.
- En el bloque `finally`, siempre imprima un mensaje como "Gracias por usar el programa".

---

### ✅ Ejercicio 5: Leer archivo con manejo de excepción
Escribe un programa que intente abrir un archivo llamado `datos.txt` y lea su contenido. Si el archivo no existe, captura la excepción `FileNotFoundError` y muestra un mensaje indicando que el archivo no se encontró.

---

### ✅ Ejercicio 6: Capturar cualquier excepción
Escribe un bloque `try-except` genérico que capture cualquier error que ocurra al ejecutar este código:

```python
resultado = 10 / 0
```

Imprime el tipo de error usando `type(e).__name__`.

---

### ✅ Ejercicio 7: Validar edad con excepción personalizada
Solicita al usuario que ingrese su edad. Si la edad es negativa, lanza una excepción `ValueError` con un mensaje personalizado.

💡 Usa:

```python
raise ValueError("La edad no puede ser negativa.")
```

---

### ✅ Ejercicio 8: Uso básico de `finally`
Escribe un programa que abra un archivo (aunque no exista), intente leerlo y use `finally` para cerrarlo o mostrar un mensaje de limpieza, incluso si hay un error.

