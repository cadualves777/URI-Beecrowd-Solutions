while True:
    try:
        x = int(input())
        l = list(map(int, input().split()))
        m = 0
        for i in range(x):
            if l[i] > m:
                m = l[i]
        
        if m < 10: print(1)
        elif m < 20: print(2)
        else: print(3)
    except EOFError:
        break
