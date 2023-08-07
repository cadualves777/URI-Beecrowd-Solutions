c = int(input())
for _ in range(c):
    fib = [0, 1]
    x = int(input())
    for i in range(2, x+1):
        num = fib[i-2] + fib[i-1]
        fib.append(num)
    print(f'Fib({x}) = {fib[x]}')
