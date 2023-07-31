lados = list(map(float, input().split()))
l_ordem = sorted(lados)
l_ordem.reverse()

a, b, c = l_ordem[0], l_ordem[1], l_ordem[2]
if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    else:
        print('TRIANGULO RETANGULO')
    if a == b and a == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
