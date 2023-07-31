vert = input()
subc = input()
comida = input()

if vert == 'vertebrado':
    if subc == 'ave':
        if comida == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if comida == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if subc == 'inseto':
        if comida == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if comida == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
