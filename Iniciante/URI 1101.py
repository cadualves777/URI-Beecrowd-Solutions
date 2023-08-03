m, n = map(int, input().split())
while m > 0 and n > 0:
    tot = 0
    if m > n:
        m, n = n, m
    for i in range(m, n+1):
        tot += i
        print(i, end=' ')
    print(f'Sum={tot}')
    m, n = map(int, input().split())
