while True:
    try:
        vol = float(input())
        diam = float(input())
        r = diam / 2
        area = 3.14 * pow(r, 2)
        h = vol / area
        print(f'ALTURA = {h:.2f}')
        print(f'AREA = {area:.2f}')
    except EOFError:
        break
