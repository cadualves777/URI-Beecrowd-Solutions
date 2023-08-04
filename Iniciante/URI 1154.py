tot = c = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    tot += idade
    c += 1
media = tot / c
print(f'{media:.2f}')
