x = int(input())
n = al = 0
for _ in range(x):
    a, b = input().split()
    if float(b) > n:
        n = float(b)
        al = a
if n >= 8:
    print(al)
else:
    print('Minimum note not reached')
