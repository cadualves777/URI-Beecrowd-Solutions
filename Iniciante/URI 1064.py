tot = cont = 0
for _ in range(6):
    x = float(input())
    if x > 0:
        tot += x
        cont += 1
media = tot / cont
print(f'{cont} valores positivos')
print(f'{media:.1f}')
