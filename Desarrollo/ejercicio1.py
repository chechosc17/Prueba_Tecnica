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
