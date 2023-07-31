a, b, c = map(float, input().split())
if (a+b) > c and (a+c) > b and (b+c) > a:
    tot = a + b + c
    print(f'Perimetro = {tot:.1f}')
else:
    tot = ((a+b)*c)/2
    print(f'Area = {tot:.1f}')
