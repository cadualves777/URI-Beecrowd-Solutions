lin = int(input())
op = input()
tam = 12
matriz = []

for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(float(input()))
    matriz.append(linha)

s = 0

for val in matriz[lin]:
    s += val

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/tam):.1f}')
