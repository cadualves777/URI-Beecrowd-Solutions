a, b = map(float, input().split())
dif = b - a
porc = 100 * dif / a
print(f'{porc:.2f}%')
