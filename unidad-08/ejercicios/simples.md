

## 🧩 Ejercicios sobre Tuplas

### ✅ Ejercicio 1: Crear tuplas
Crea una tupla llamada `mis_datos` con tu nombre (como string), edad (como entero) y ciudad (como string).  
Imprime la tupla.

### ✅ Ejercicio 2: Acceder a elementos
Dada la tupla:
```python
colores = ("rojo", "verde", "azul")
```
- Imprime el primer color.
- Imprime el último color usando un índice negativo.

### ✅ Ejercicio 3: Iterar sobre una tupla
Usa un bucle `for` para imprimir cada elemento de la tupla `colores`, pero convertido a mayúsculas.

### ✅ Ejercicio 4: Usar operadores
Dadas las tuplas:
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
```
- Une ambas tuplas en una nueva llamada `tupla_unida`.
- Multiplica `tupla1` por 2 y guárdala en `tupla_doble`.

### ✅ Ejercicio 5: Verificar existencia
Dada la tupla:
```python
numeros = (10, 20, 30, 40, 50)
```
Verifica si el número `30` está en la tupla y muestra un mensaje según sea cierto o falso.

---

## 📚 Ejercicios sobre Diccionarios

### ✅ Ejercicio 6: Crear diccionario
Crea un diccionario llamado `mi_perfil` con las siguientes claves: `"nombre"`, `"apellido"`, `"edad"` y `"ciudad"`.  
Asigna tus datos reales como valores.

Imprime todo el diccionario.

### ✅ Ejercicio 7: Acceder a valores
Usando el diccionario del ejercicio anterior, imprime solo el valor de `"ciudad"`.

### ✅ Ejercicio 8: Modificar valores
Modifica el valor de `"edad"` en el diccionario `mi_perfil` y luego imprime el diccionario actualizado.

### ✅ Ejercicio 9: Agregar nuevas claves
Agrega una nueva clave `"correo"` al diccionario `mi_perfil` con tu correo electrónico ficticio.  
Imprime el diccionario actualizado.

### ✅ Ejercicio 10: Eliminar claves
Elimina la clave `"apellido"` del diccionario `mi_perfil`.  
Imprime el resultado final.

---

## 🔄 Ejercicios combinados (Tuplas + Diccionarios)

### ✅ Ejercicio 11: Diccionario con tuplas como valores
Crea un diccionario llamado `coordenadas` donde las claves sean nombres de ciudades y los valores sean tuplas con sus coordenadas (latitud y longitud).  
Ejemplo:
```python
coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid": (40.4168, -3.7038)
}
```

Imprime las coordenadas de una ciudad específica (por ejemplo, `"Madrid"`).

### ✅ Ejercicio 12: Iterar sobre un diccionario con tuplas
Usa un bucle `for` para recorrer el diccionario `coordenadas` del ejercicio anterior e imprime en pantalla:
```
Ciudad: Buenos Aires → Latitud: -34.6037, Longitud: -58.3816
```

### ✅ Ejercicio 13: Métodos del diccionario
Dado el siguiente diccionario:
```python
productos = {
    "manzana": 1.5,
    "banana": 0.9,
    "leche": 2.3
}
```

- Usa el método `.keys()` y un bucle para imprimir todas las claves.
- Usa el método `.values()` y un bucle para imprimir todos los precios.
- Usa el método `.items()` para imprimir cada par clave-valor en este formato:
  ```
  Producto: manzana → Precio: $1.5
  ```

---

