x = int(input())
while x != 0:
    if x % 2 == 1:
        x += 1
    tot = 0
    for _ in range(5):
        tot += x
        x += 2
    print(tot)
    x = int(input())
