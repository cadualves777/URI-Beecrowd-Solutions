def ehMaior(x, y):
  maior = (x + y + abs(x-y)) / 2
  return int(maior)

a, b, c = map(int, input().split())
maior = ehMaior(a, b)
if c > maior:
  maior = c
print(f'{maior} eh o maior')
