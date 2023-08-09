a, b  = map(int, input().split())
q, r = a//b, a%b
if r<0:
    q += 1
    r -= b
print(f'{q} {r}')
