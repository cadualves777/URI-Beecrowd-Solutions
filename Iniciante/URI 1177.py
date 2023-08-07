x = int(input())
n = []
num = 0
for i in range(1000):
    if num == x:
        num = 0
    n.append(num)
    print(f'N[{i}] = {n[i]}')
    num += 1
