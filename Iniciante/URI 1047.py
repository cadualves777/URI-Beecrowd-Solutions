hi, mi, hf, mf = map(int, input().split())
hr = hf - hi
mn = mf - mi
if mn < 0:
    mn += 60
    hr -= 1
if hr < 0:
    hr += 24
if hr == 0 and mn == 0:
    hr, mn = 24, 0
    
print(f'O JOGO DUROU {hr} HORA(S) E {mn} MINUTO(S)')
