notas = []
res = 1
while res != 2:
    if res < 1 or res > 2:
        res = int(input('novo calculo (1-sim 2-nao)\n'))
    else:
        while len(notas) < 2:
            nota = float(input())
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print('nota invalida')
        media = (notas[0] + notas[1]) / 2
        print(f'media = {media:.2f}')
        notas = []
        res = int(input('novo calculo (1-sim 2-nao)\n'))
