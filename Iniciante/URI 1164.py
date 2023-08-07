x = int(input())
for _ in range(x):
    n = int(input())
    t = 0
    for num in range(1, n):
        if n % num == 0:
            t += num
    if t == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
