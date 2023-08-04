x = int(input())
for _ in range(x):
    a, b = map(int, input().split())
    tot = 0
    if a % 2 == 0:
        a += 1
    for i in range(b):
        tot += a
        a += 2
    print(tot)
