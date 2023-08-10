n, m = map(int, input().split())
while n != 0 and m != 0:
    if (m-n) <= 3 or (m-n) > 200:
        print('impossible')
    else:
        print('possible')
    n, m = map(int, input().split())
