x, y = map(int, input().split())
while x != 0 and y != 0:
    if x > 0 and y > 0: print('primeiro')
    if x < 0 and y > 0: print('segundo')
    if x < 0 and y < 0: print('terceiro')
    if x > 0 and y < 0: print('quarto')
    x, y = map(int, input().split())
