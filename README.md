# Práctica - Alineación de Cadenas

Esta práctica consiste en realizar la **alineación de dos cadenas utilizando programación dinámica**.

El programa recibe dos cadenas ingresadas por el usuario y construye una matriz para encontrar el costo mínimo de alinearlas. Para realizar el proceso se consideran las coincidencias entre caracteres, las diferencias y los espacios o gaps.

## ¿Qué hace el programa?

El programa permite ingresar dos cadenas y realiza los siguientes pasos:

1. Crea la matriz inicial de costos.
2. Completa la primera fila y columna considerando los gaps.
3. Calcula el costo de cada posición de la matriz.
4. Encuentra la alineación con el menor costo.
5. Muestra las dos cadenas alineadas.
6. Indica el costo mínimo obtenido.
7. Muestra las operaciones que se realizaron para llegar a la alineación.

La matriz se construye comparando los caracteres de las dos cadenas y tomando entre las diferentes opciones el costo mínimo.

## Programación dinámica

La solución utiliza programación dinámica para evitar resolver repetidamente los mismos subproblemas. Primero se construye la matriz y después se utiliza para reconstruir la alineación final.

Durante la reconstrucción se pueden encontrar operaciones como:

* Sustitución de un carácter.
* Borrado de un carácter.
* Inserción de un carácter.

Estas operaciones se obtienen recorriendo la matriz desde la posición final hasta llegar al inicio.

## ¿Cómo ejecutar el programa?

Se necesita tener Python instalado.

Desde la carpeta donde se encuentra el archivo se puede ejecutar:

```bash
python alineacion_cadenas.py
```

El programa solicitará las dos cadenas:

```text
Ingrese la primera cadena:
Ingrese la segunda cadena:
```

Después mostrará la matriz resultante, las cadenas alineadas, el costo mínimo y las operaciones encontradas.

## Ejemplo de funcionamiento

Si se ingresan dos cadenas diferentes, el programa compara sus caracteres y determina qué cambios son necesarios para conseguir una alineación con el menor costo.

Las penalidades utilizadas en la práctica están establecidas en `1`, por lo que cada diferencia, inserción o borrado tiene el mismo costo durante la prueba.

## Archivos

```text
practica-alineacion-cadenas/
│
├── alineacion_cadenas.py
└── README.md
```

## Tema

**Programación Dinámica - Alineación de Cadenas**
