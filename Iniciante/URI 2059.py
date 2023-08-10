p, j1, j2, r, a = input().split()
res = (int(j1) + int(j2)) % 2
if (r == '1') and (a == '1'):
    print('Jogador 2 ganha!')
elif (r == '1') or (a == '1'):
    print('Jogador 1 ganha!')
else:
    if res == 0:
        if p == '1':
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')
    elif res == int(p):
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')
