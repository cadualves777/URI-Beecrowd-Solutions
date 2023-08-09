A, B, C, D = map(int, input().split())

def forma_triangulo(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)

if forma_triangulo(A, B, C) or forma_triangulo(A, B, D) or forma_triangulo(A, C, D) or forma_triangulo(B, C, D):
    print('S')
else:
    print('N')
