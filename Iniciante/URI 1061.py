entrada_diai = input().split()
diai = int(entrada_diai[1])
entrada_horai = input().replace(' : ', ':').split(':')
hi, mi, si = int(entrada_horai[0]), int(entrada_horai[1]), int(entrada_horai[2])

entrada_diaf = input().split()
diaf = int(entrada_diaf[1])
entrada_horaf = input().replace(' : ', ':').split(':')
hf, mf, sf = int(entrada_horaf[0]), int(entrada_horaf[1]), int(entrada_horaf[2])

dia = diaf - diai
hr = hf - hi
mn = mf - mi
sg = sf - si

if sg < 0:
    sg += 60
    mn -= 1
if mn < 0:
    mn += 60
    hr -= 1
if hr < 0:
    hr += 24
    dia -= 1
    
print(f'{dia} dia(s)')
print(f'{hr} hora(s)')
print(f'{mn} minuto(s)')
print(f'{sg} segundo(s)')
