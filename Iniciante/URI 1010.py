tot = 0
for _ in range(2):
  entrada = input().split()
  tot += int(entrada[1]) * float(entrada[2])
print(f'VALOR A PAGAR: R$ {tot:.2f}')
