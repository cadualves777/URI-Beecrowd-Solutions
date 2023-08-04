vals = list(map(int, input().split()))
tot = 0
i = 1
while vals[i] <= 0:
    if vals[i] <= 0:
        i += 1
    if vals[i] > 0:
        break

for x in range(vals[i]):
    tot += vals[0] + x

print(tot)
