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

for i in range(tam):
    for j in range(tam):
        if j < i:
            s += matriz[i][j]

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/div):.1f}')
