x = int(input())
for _ in range(x):
    j1, op1, j2, op2 = input().split()
    n1, n2 = map(int, input().split())
    res = n1 + n2
    if res % 2 == 0:
        if op1 == 'PAR':
            print(j1)
        else:
            print(j2)
    else:
        if op1 == 'IMPAR':
            print(j1)
        else:
            print(j2)
