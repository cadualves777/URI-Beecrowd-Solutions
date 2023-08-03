x = int(input())
for _ in range(x):
    par = res = ''
    n = int(input())
    if n == 0:
        print('NULL')
    else:
        if n % 2 == 0:
            par = 'EVEN'
        else:
            par = 'ODD'
        if n > 0:
            res = 'POSITIVE'
        else:
            res = 'NEGATIVE'
        print(f'{par} {res}')
