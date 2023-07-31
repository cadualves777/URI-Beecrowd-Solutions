hi, hf = map(int, input().split())
if hi > hf:
    hr = hf - hi + 24
elif hi < hf:
    hr = hf - hi
else:
    hr = 24
print(f'O JOGO DUROU {hr} HORA(S)')
