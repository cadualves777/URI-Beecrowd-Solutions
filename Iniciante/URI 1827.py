def cria_matriz(o):
    m = [[0] * o for _ in range(o)]

    inicio = o // 3
    fim = o - inicio

    for i in range(o):
        m[i][i] = 2
        m[i][o - i - 1] = 3

    for i in range(inicio, fim):
        for j in range(inicio, fim):
            m[i][j] = 1

    c = o // 2
    m[c][c] = 4

    return m

def imprime_matriz(m):
    for l in m:
        print("".join(map(str, l)))

while True:
    try:
        ordem = int(input())
        matriz = cria_matriz(ordem)
        imprime_matriz(matriz)
        print()
    except EOFError:
        break
