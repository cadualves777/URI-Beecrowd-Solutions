tot = c = r = s = 0
n = int(input())
for _ in range(n):
    ent = input().split()
    qtd, animal = int(ent[0]), ent[1]
    tot += qtd
    if animal == 'C':
        c += qtd
    elif animal == 'R':
        r += qtd
    else:
        s += qtd

pct_c = (c/tot) * 100
pct_r = (r/tot) * 100
pct_s = (s/tot) * 100

print(f'Total: {tot} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {pct_c:.2f} %')
print(f'Percentual de ratos: {pct_r:.2f} %')
print(f'Percentual de sapos: {pct_s:.2f} %')
