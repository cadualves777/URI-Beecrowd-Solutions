casos = int(input())
for i in range(casos):
    pA, pB, cA, cB = map(float, input().split())
    pA, pB = int(pA), int(pB)
    anos = 0
    
    while pA <= pB:
        pA += int((pA*cA) / 100)
        pB += int((pB*cB) / 100)
        anos += 1
        
        if anos > 100:
            break
    
    if anos <= 100: print(f'{anos} anos.')
    else: print('Mais de 1 seculo.')
