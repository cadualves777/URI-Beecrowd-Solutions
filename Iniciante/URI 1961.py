hp, p = map(int, input().split())
pulos = list(map(int, input().split()))
v = True
for i in range(1, p):
    if abs(pulos[i] - pulos[i-1]) > hp:
        v = False
        break
if v: print('YOU WIN')
else: print('GAME OVER')
