from math import sqrt

while True:
    x = input()
    if x == '0':
        break
    a, b, c = x.split()
    area = int(a) * int(b)
    area_perm = area * 100 / int(c)
    lado = int(sqrt(area_perm))
    print(lado)
