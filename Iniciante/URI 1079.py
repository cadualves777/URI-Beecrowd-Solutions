n = int(input())
for _ in range(n):
    n1, n2, n3 = map(float, input().split())
    media = (2*n1 + 3*n2 + 5*n3) / 10
    print(f'{media:.1f}')
