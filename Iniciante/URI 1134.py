a = g = d = 0
c = int(input())
while c != 4:
    if c == 1:
        a += 1
    elif c == 2:
        g += 1
    elif c == 3:
        d += 1
    c = int(input())
print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')
