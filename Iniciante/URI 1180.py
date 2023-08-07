x = int(input())
nums = list(map(int, input().split()))
menor = 1000
for i in range(x):
    if nums[i] < menor:
        menor = nums[i]
        pos = i
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
