imp = par = pos = neg = 0
for _ in range(5):
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        imp += 1
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1

print(f'{par} valor(es) par(es)')
print(f'{imp} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
