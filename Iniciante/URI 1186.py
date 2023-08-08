op = input()
tam = 12
matriz = []
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(float(input()))
    matriz.append(linha)

s = c = 0
div = ((tam**2) - tam) / 2


for i in range(tam-1, 0, -1):
    c += 1
    for j in range(c, tam):
        s += matriz[i][j]

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/div):.1f}')
