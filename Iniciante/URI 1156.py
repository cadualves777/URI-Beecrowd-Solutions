s = 0
n = d = 1
while n != 39:
    s += n/d
    n += 2
    d *= 2
print(f'{s:.2f}')
