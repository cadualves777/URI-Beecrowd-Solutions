x = int(input())
i = 1
cont = 0
while cont < x:
    for _ in range(3):
        print(i, end=' ')
        i += 1
    i += 1
    print('PUM')
    cont += 1
