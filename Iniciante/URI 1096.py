i, j = 1, 7
while i <= 9:
    for _ in range(3):
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j = 7
