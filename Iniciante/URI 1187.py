op = input()
tam = 12
matriz = []
for i in range(tam):
    linha = []
    for j in range(tam):
        linha.append(float(input()))
    matriz.append(linha)

s = 0
div = ((tam**2) - (tam*2)) / 4
inf = 1
sup = 11

for i in range(int((tam-1)/2)):
    for j in range(inf, sup):
        s += matriz[i][j]
    inf += 1
    sup -= 1

if op == 'S':
    print(f'{s:.1f}')
elif op == 'M':
    print(f'{(s/div):.1f}')
