while True:
    x = int(input())
    if x == 0:
        break
    for _ in range(x):
        y = int(input())
        if y % 2 == 0:
            t = (y*2) - 2
        else:
            t = (y*2) - 1
        print(t)
