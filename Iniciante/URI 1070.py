x = int(input())
cont = 0
while cont < 6:
    if x % 2 == 0:
        x += 1
    print(x)
    x += 2
    cont += 1
