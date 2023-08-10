x = int(input())
nums = list(map(int, input().split()))
div = [2, 3, 4, 5]
for d in div:
    c = 0
    for n in nums:
        if n % d == 0:
            c += 1
    print(f'{c} Multiplo(s) de {d}')
