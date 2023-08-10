while True:
    try:
        m, d = map(int, input().split())
        dias_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
        if m == 12 and d == 24: print('E vespera de natal!')
        elif m == 12 and d == 25: print('E natal!')
        elif m == 12 and d > 25: print('Ja passou!')
        else:
            dias_falt = dias_mes[m-1] - d
            for i in range(m, 12):
                dias_falt += dias_mes[i]
            print(f'Faltam {dias_falt} dias para o natal!')
    except EOFError:
        break
