def ehPrimo(n):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True

x = int(input())
for _ in range(x):
    num = int(input()) 
    if ehPrimo(num):
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
