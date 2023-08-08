def imprimir_matriz(matriz):
    if not matriz:
        return

    tamanho_max = len(str(max(map(max, matriz))))
    for linha in matriz:
        linha_formatada = [str(valor).rjust(tamanho_max) for valor in linha]
        print(' '.join(linha_formatada))
    print()


tam = int(input())
while tam > 0:
    matriz = []
    el = aux = 1
    for i in range(tam):
        linha = []
        for j in range(tam):
            linha.append(el)
            el *= 2
        matriz.append(linha)
        aux *= 2
        el = aux
        
    imprimir_matriz(matriz)
    tam = int(input())
