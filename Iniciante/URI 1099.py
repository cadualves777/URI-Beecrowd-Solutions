n = int(input())
for _ in range(n):
    tot = 0
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    for i in range(x+1, y):
        if i % 2 == 1:
            tot += i
    print(tot)
