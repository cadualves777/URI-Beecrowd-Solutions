n = float(input())
cont = tot = 0
while cont < 2:
    if 0 <= n <= 10:
        tot += n
        cont += 1
    else:
        print('nota invalida')
    n = float(input())
media = tot / 2
print(f'media = {media:.2f}')
