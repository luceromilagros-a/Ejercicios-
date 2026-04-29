
## 🧠 Ejercicios Avanzados

---

### 🔢 **Ejercicio 1: Conteo de Palabras Únicas**
Dada una lista de frases (strings), crea un diccionario donde las claves sean las palabras únicas y los valores sean la cantidad de veces que aparecen en todas las frases.

- Usa `split()` para dividir las palabras.
- Convierte todo a minúsculas.
- Ignora signos de puntuación (`.,!?`).
- Muestra el diccionario final ordenado alfabéticamente por palabra.

```python
frases = [
    "Hola mundo",
    "Mundo, hola!",
    "Python es genial",
    "Hola de nuevo"
]
```

---

### 📈 **Ejercicio 2: Análisis de Ventas por Producto**
Tienes un diccionario donde cada clave es el nombre de un producto y el valor es una tupla con las ventas mensuales de ese producto (una tupla de números).

Crea un programa que:
- Calcule el total de ventas por producto.
- Determine cuál producto tiene mayores ventas totales.
- Imprima un ranking de productos según sus ventas totales.

```python
ventas = {
    "Producto A": (1200, 1500, 900),
    "Producto B": (800, 700, 1000),
    "Producto C": (2000, 1800, 1700)
}
```

---

### 🗺️ **Ejercicio 3: Distancia entre Coordenadas**
Usa un diccionario con coordenadas geográficas (como tuplas) similar al del PDF.

Implementa una función que calcule la distancia entre dos ciudades usando la fórmula de distancia euclidiana simplificada:

```
distancia = √(x2 - x1)^2 + (y2 - y1)^2
```

Y luego permite al usuario elegir dos ciudades y mostrar la distancia entre ellas.

```python
coordenadas = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Madrid": (40.4168, -3.7038),
    "Roma": (41.9028, 12.4964),
    "Tokio": (35.6895, 139.6917)
}
```

---

### 📊 **Ejercicio 4: Registro de Estudiantes con Menú Interactivo**
Crea un programa que permita gestionar un registro de estudiantes mediante un menú interactivo.

El programa debe usar un diccionario donde las claves sean los IDs de los estudiantes y los valores sean tuplas con su nombre, edad y promedio.

Menú:
1. Agregar estudiante
2. Mostrar todos los estudiantes
3. Buscar estudiante por ID
4. Eliminar estudiante por ID
5. Salir

Usa bucles `while` y `if/elif/else` para crear este menú.

---

### 🧮 **Ejercicio 5: Promedio de Calificaciones por Curso**
Tienes un diccionario donde las claves son nombres de cursos y los valores son listas de calificaciones (enteros). Escribe un programa que:

- Calcule el promedio de calificaciones por curso.
- Identifique el curso con mejor promedio.
- Identifique el curso con peor promedio.

```python
calificaciones = {
    "Matemáticas": [85, 90, 78, 92],
    "Historia": [70, 65, 80, 72],
    "Ciencias": [88, 91, 85, 87]
}
```

---

### 🕹️ **Ejercicio 6: Juego de Preguntas y Respuestas**
Crea un juego tipo trivia con preguntas almacenadas en una lista de tuplas. Cada tupla contiene la pregunta, las opciones y la respuesta correcta.

El jugador debe responder preguntas y acumular puntos.

Ejemplo de estructura:
```python
preguntas = [
    ("¿Cuál es la capital de Argentina?", ["Buenos Aires", "Lima", "Santiago"], "Buenos Aires"),
    ("¿En qué año se fundó Python?", ["1991", "1989", "2000"], "1991")
]
```

Características:
- Usar bucle `for` para recorrer preguntas.
- Validar respuesta con `if`.
- Usar contador de aciertos.
- Mostrar resultado final.

---

### 🧾 **Ejercicio 7: Inventario de Productos con Búsqueda Dinámica**
Tienes un inventario de productos como diccionario. Las claves son los códigos de los productos y los valores son tuplas con (nombre, precio, stock).

Permite al usuario:
- Ver todo el inventario.
- Buscar productos por nombre (mostrar coincidencias).
- Filtrar productos por rango de precio.
- Actualizar stock de un producto.
- Eliminar un producto del inventario.

Estructura inicial:
```python
inventario = {
    101: ("Camiseta", 25.99, 50),
    102: ("Pantalón", 49.99, 30),
    103: ("Zapatos", 79.99, 20)
}
```

---

