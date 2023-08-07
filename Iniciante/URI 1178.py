x = []
n = float(input())
for i in range(100):
    x.append(n)
    n /= 2
    print(f'N[{i}] = {x[i]:.4f}')
