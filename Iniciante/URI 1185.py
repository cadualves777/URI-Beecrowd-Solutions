op = input()
tam = 12
matriz = []
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(float(input()))
    matriz.append(linha)

s = 0
div = ((tam**2) - tam) / 2
c = tam

for i in range(tam-1):
    c -= 1
    for j in range(c):
        s += matriz[i][j]

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/div):.1f}')
