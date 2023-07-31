def sal4500(s):
    tot = s - 4500
    return tot * 0.28

def sal3000(s):
    tot = s - 3000
    return tot * 0.18

def sal2000(s):
    tot = s - 2000
    return tot * 0.08

sal = float(input())
total = 0
if sal <= 2000.00:
    print('Isento')
else:
    if sal > 4500:
        total += sal4500(sal)
        sal -= (sal - 4500)
    
    if sal > 3000:
        total += sal3000(sal)
        sal -= (sal - 3000)
    
    if sal > 2000:
        total += sal2000(sal)
        sal -= (sal - 2000)
    
    print(f'R$ {total:.2f}')
