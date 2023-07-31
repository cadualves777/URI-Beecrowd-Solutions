nums = []
cont = 0
for i in range(6):
    nums.append(float(input()))
for n in nums:
    if n > 0:
        cont += 1
print(f'{cont} valores positivos')
