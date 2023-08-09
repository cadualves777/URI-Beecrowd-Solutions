c = 0
while c < 3:
    res = 0
    while True:
        ent = input()
        if ent == 'caw caw':
            break
        num_bin = ent.replace('-', '0').replace('*', '1')
        dec = int(num_bin, 2)
        res += dec
    print(res)
    c += 1
