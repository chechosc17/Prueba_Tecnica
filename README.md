# Prueba Técnica en Python

Este repositorio contiene los resultados de una prueba técnica en la que se resolvieron 4 ejercicios utilizando el lenguaje de programación Python en Visual Studio Code, 
los ejercicios abarcan diversos conceptos de programación, desde bucles y estructuras de control hasta manejo de listas y funciones.

## Ejercicio 1: Clasificación de Números

El primer ejercicio consiste en clasificar números en diferentes categorías y calcular un total de puntos. El código se encuentra en el archivo `ejercicio1.py`.

```python
listaNum = [1, 2, 3, 4, 5]
total = 0

for value in listaNum:
    if value % 2 == 0:
        print(f'El numero par ({value} da 1 punto)')
        total = total + 1
    elif value % 2 != 0 and value != 5:
        print(f'El numero impar ({value} da 3 puntos)')
        total = total + 3
    elif value == 5:
        print(f'El numero 5 da 5 puntos')
        total = total + 5

print(f'El total es: {total}') # Resultado: 13
```
## Ejercicio 2: Serie Tribonacci

El segundo ejercicio implica la generación de una serie Tribonacci a partir de un conjunto inicial de valores, validando que los tres números ingresados inicialmente sean validos bajo la Fibonacci original. El código se encuentra en el archivo `ejercicio2.py`.

```python
def validarFibonacci(dataArray):
    if dataArray[0] == dataArray[1] and dataArray[1] != 1:
        return False
    if dataArray[0] + dataArray[1] == dataArray[2]:
        return True
    else:
        return False

def tribonacci(valor):
    tribon = []
    if validarFibonacci(valor):
        a, b, c = valor[0], valor[1], valor[2]
        for i in range(6):
            tribon.append(a)
            a, b, c = b, c, a + b + c
        return tribon
    else:
        return 'La secuencia inicial no corresponde a una secuencia Fibonacci válida'

print(f'Tribonacci: {tribonacci([1, 1, 2])}')  # Resultado: [1, 1, 2, 4, 7, 13]
print(f'Tribonacci: {tribonacci([1, 2, 3])}')  # Resultado: [1, 2, 3, 6, 11, 20]
print(f'Tribonacci: {tribonacci([3, 5, 8])}')  # Resultado: [3, 5, 8, 16, 29, 53]
```

## Ejercicio 3: Transformación de Listas

El tercer ejercicio trata sobre la transformación de una lista según ciertos criterios definidos por un diccionario de entrada. El código se encuentra en el archivo `ejercicio3.py`. 

```python
dato = {
    "tipo": 1,
    "numeros": [2, 3, 1, 1]
}

def transformarLista(dato):
    listaPredeterminada = [2, 3, 1, 1, 3, 2, 1, 4]
    tipo = dato["tipo"]
    lista = listaPredeterminada + dato["numeros"]
    resultado = []

    if tipo == 1:
        for valor in lista:
            if valor not in resultado:
                resultado.append(valor)
    elif tipo == 2:
        for valor in lista:
            if valor == 1 or valor == 3:
                resultado.append(valor)
    elif tipo == 3:
        resultado = sorted(lista)
    
    return resultado

print(f'Salida: {transformarLista(dato)}')
```

## Ejercicio 4: Manipulación de listas

El cuarto ejercicio implica la manipulación y suma de dos listas. El código se encuentra en el archivo `ejercicio4.py`.

```python
def leerNumero():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 30: "))
            if 1 <= numero <= 30:
                return numero
            else:
                print("El número debe estar entre 1 y 30.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

n = int(input("Ingrese cuántos datos desea leer (máximo 15): "))
if n > 15:
    n = 15

lista1 = []
lista2 = []

print("\nIngrese los datos para la lista1:")
for _ in range(n):
    numero = leerNumero()
    lista1.append(numero)

print("\nIngrese los datos para la lista2:")
for _ in range(n):
    numero = leerNumero()
    lista2.append(numero)

lista1.sort()
lista2.sort()

print("\nLista1 ordenada:", lista1)
print("Lista2 ordenada:", lista2)

sumaListas = []
for i in range(n):
    sumaListas.append(lista1[i] + lista2[i])

print("\nSuma de listas:", sumaListas)
```

## Requisitos ⚙️

Asegúrate de tener Python instalado en tu sistema para poder ejecutar los scripts. Además, puedes utilizar un entorno de desarrollo como Visual Studio Code para una experiencia de codificación más cómoda.
Si no deseas ejecutarlo localmente puedes optar por entornos de ejecución online como:
* [www.programiz.com](https://www.programiz.com/python-programming/online-compiler/) - Compilador online
* [www.online-python.com](https://www.online-python.com/) - Compilador online

### Instrucciones de Ejecución 📋
1. Clona este repositorio en tu máquina local.
2. Abre los archivos de cada ejercicio en tu entorno de desarrollo preferido (por ejemplo, Visual Studio Code).
3. Ejecuta los scripts.


## Herramientas usadas para el desarrollo 🛠️

* [Visual Studio Code](https://code.visualstudio.com/) - Es un editor de código fuente desarrollado por Microsoft

## Lenguaje de programación utilizado para el desarrollo 💻
* [Python](https://developer.mozilla.org/es/docs/Web/JavaScript) - Lenguaje de programación
