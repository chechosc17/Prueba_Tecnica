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
