cardapio = [0.0, 4.0, 4.5, 5.0, 2.0, 1.5]
cod, qtd = map(int, input().split())
total = cardapio[cod] * qtd
print(f'Total: R$ {total:.2f}')
