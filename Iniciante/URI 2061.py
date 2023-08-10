abas, x = map(int, input().split())
for _ in range(x):
    acao = input()
    if acao == 'fechou':
        abas += 1
    elif acao == 'clicou':
        abas -= 1
print(abas)
