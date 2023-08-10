atual = 2015
n = int(input())
for i in range(n):
    num = int(input())
    tempo = atual - num
    if tempo <= 0:
        print(f'{abs(tempo)+1} A.C.')
    else:
        print(f'{tempo} D.C.')
