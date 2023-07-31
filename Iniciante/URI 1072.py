x = int(input())
dentro = fora = 0
for _ in range(x):
    y = int(input())
    if 10 <= y <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} in')
print(f'{fora} out')
