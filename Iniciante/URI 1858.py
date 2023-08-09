m = 20
n = int(input())
t = list(map(int, input().split()))
for i in range(n):
    if t[i] < m:
        m = t[i]
        pos = i + 1
    elif t[i] == m:
        m = t[i]
print(pos)
