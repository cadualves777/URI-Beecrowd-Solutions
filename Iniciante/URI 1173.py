x = [int(input())]
print(f'N[0] = {x[0]}')
for i in range(9):
    x.append(x[i]*2)
    print(f'N[{i+1}] = {x[i+1]}')
