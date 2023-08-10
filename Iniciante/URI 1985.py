x = int(input())
prods = {1001:1.5, 1002:2.5, 1003:3.5, 1004:4.5, 1005:5.5}
t = 0
for _ in range(x):
    cod, qtd = map(int, input().split())
    t += prods[cod] * qtd
print(f'{t:.2f}')
