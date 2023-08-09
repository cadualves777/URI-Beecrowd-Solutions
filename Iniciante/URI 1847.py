a, b, c = map(int, input().split())
if a > b:
    if b <= c: print(':)')
    else:
        if (a-b) > (b-c): print(':)')
        else: print(':(')
elif a < b:
    if b >= c: print(':(')
    else:
        if (b-a) > (c-b): print(':(')
        else: print(':)')
else:
    if b < c: print(':)')
    else: print(':(')
