def criar_matriz(tamanho):
    matriz = [[3 for _ in range(tamanho)] for _ in range(tamanho)]
    for i in range(tamanho):
        matriz[i][i] = 1
        matriz[i][tamanho - i - 1] = 2
    return matriz

while True:
    try:
        tam = int(input())
        m = criar_matriz(tam)
        for l in m:
            for e in l:
                print(e, end='')
            print()
    except EOFError:
        break
