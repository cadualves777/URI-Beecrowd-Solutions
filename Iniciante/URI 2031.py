n = int(input())
for i in range(n):
    jog1 = input()
    jog2 = input()
    if jog1 == 'pedra':
        if jog2 == 'pedra':
            res = 'Sem ganhador'
        elif jog2 == 'papel':
            res = 'Jogador 1 venceu'
        elif jog2 == 'ataque':
            res = 'Jogador 2 venceu'
    elif jog1 == 'papel':
        if jog2 == 'pedra':
            res = 'Jogador 2 venceu'
        elif jog2 == 'papel':
            res = 'Ambos venceram'
        elif jog2 == 'ataque':
            res = 'Jogador 2 venceu'
    elif jog1 == 'ataque':
        if jog2 == 'pedra':
            res = 'Jogador 1 venceu'
        elif jog2 == 'papel':
            res = 'Jogador 1 venceu'
        elif jog2 == 'ataque':
            res = 'Aniquilacao mutua'
    print(res)
