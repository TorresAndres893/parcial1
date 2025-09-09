
# Parcial 1 – Lenguajes de Programación

## Enunciados y Comandos de Ejecución

**Punto 1**  
Para el siguiente ejercicio, dé una expresión regular que represente el conjunto descrito:  
El conjunto de cadenas sobre {a, b, c} en el cual todas las `a` preceden a las `b` y éstas a su vez preceden a las `c`.  
Es posible que no haya `a`, `b` o `c`. Implemente el AFD para esta expresión regular. Use Python.  

**Comando de ejecución:**  
```bash
python3 AFD.py
````

---

**Punto 2**
Si la expresión regular para un ID es la siguiente: `[A-Za-z][A-Za-z0-9]*`.
Implemente un AFD en Python. Realice mínimo 5 pruebas, tres donde **ACEPTE** y dos donde **NO ACEPTE**.

**Comando de ejecución:**

```bash
python3 Expresion.py
```

---

**Punto 3**
Escriba un programa en C que implemente una calculadora que pueda sacar raíz cúbica de números reales.
Use Flex y Bison. La entrada debe ser por un archivo de texto y la salida debe ser por consola.

---

**Punto 4**
Para el algoritmo recursivo de Euclides, implemente una comparación de rendimiento entre C como lenguaje imperativo
y Haskell, lenguaje declarativo. Haga un análisis de los resultados obtenidos.

---

**Punto 5**
Escriba un programa en ANTLR que pueda calcular los primeros `n` términos de la serie de Maclaurin para `e^x`.

**Comandos de ejecución:**

```bash
antlr4 -no-listener -visitor Grama.g4  
antlr4 Grama.g4
javac Grama*.java EvalVisitor.java Euler.java
java Euler
```
