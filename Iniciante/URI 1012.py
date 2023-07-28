a, b, c = map(float, input().split())
triang = (a * c) / 2
circ = 3.14159 * c ** 2
trap = ((a+b) * c) / 2
quad = b * b
ret = a * b
print(f'''TRIANGULO: {triang:.3f}
CIRCULO: {circ:.3f}
TRAPEZIO: {trap:.3f}
QUADRADO: {quad:.3f}
RETANGULO: {ret:.3f}''')
