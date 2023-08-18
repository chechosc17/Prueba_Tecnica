def leerNumero():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 30: "))
            if 1 <= numero <= 30:
                return numero
            else:
                print("El numero debe estar entre 1 y 30.")
        except ValueError:
            print("Entrada invalida. Intente nuevamente.")
n = int(input("Ingrese cuántos datos desea leer (Máximo deben ser 15): "))
if n > 15:
    n=15

lista1 = []
lista2 = []

print("\nIngrese los datos para la lista1: ")
for _ in range(n):
    numero = leerNumero()
    lista1.append(numero)

print("\nIngrese los datos para la lista2: ")
for _ in range(n):
    numero = leerNumero()
    lista2.append(numero)

lista1.sort()
lista2.sort()

print("\nlista1 ordenada:", lista1)
print("\nlista2 ordenada:", lista2)

sumListas = []
for i in range(n):
    sumListas.append(lista1[i] + lista2[i])

print("\nSuma de listas:", sumListas)

