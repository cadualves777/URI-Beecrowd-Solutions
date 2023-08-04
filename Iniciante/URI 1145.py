x, y = map(int, input().split())
linha = 0
for i in range(1, y+1):
    linha += 1
    if linha == x:
        print(i, end='\n')
        linha = 0
    else:
        print(i, end=' ')
