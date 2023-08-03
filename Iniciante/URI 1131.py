c = i = g = e = 0
res = 1
while res == 1:
    inter, gremio = map(int, input().split())
    c += 1
    if inter > gremio:
        i += 1
    elif gremio > inter:
        g += 1
    else:
        e += 1
    res = int(input('Novo grenal (1-sim 2-nao)\n'))

print(f'{c} grenais')
print(f'Inter:{i}')
print(f'Gremio:{g}')
print(f'Empates:{e}')

if i > g:
    print('Inter venceu mais')
elif g > i:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
