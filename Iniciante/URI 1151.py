x = int(input())
fib = [0, 1]
for i in range(1, x-1):
    y = fib[i] + fib[i-1]
    fib.append(y)
for f in fib:
    if f == fib[x-1]:
        print(f, end='\n')
    else:
        print(f, end=' ')
