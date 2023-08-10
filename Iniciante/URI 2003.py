while True:
    try:
        h, m = map(int, input().split(':'))
        h += 1
        t = 0
        if h > 8:
            t = (h - 8) * 60 + m
        elif h == 8 and m > 0:
            t = m
        print(f'Atraso maximo: {t}')
    except EOFError:
        break
