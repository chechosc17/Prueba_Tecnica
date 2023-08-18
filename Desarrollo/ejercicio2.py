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

