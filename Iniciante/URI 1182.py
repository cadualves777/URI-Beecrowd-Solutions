col = int(input())
op = input()
tam = 12
matriz = []
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(float(input()))
    matriz.append(linha)

s = 0

for i in range(tam):
    for j in range(tam):
        if j == col:
            s += matriz[i][j]

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/tam):.1f}')
