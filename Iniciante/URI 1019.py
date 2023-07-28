tempo = int(input())

h = tempo // 3600
rh = tempo % 3600
m = rh // 60
s = rh % 60

print(f'{h}:{m}:{s}')
