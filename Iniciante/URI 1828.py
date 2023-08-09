n = int(input())
for i in range(n):
    s, r = input().split()
    if s == 'papel':
        if r == 'papel': res = 'De novo!'
        elif r == 'pedra': res = 'Bazinga!'
        elif r == 'tesoura': res = 'Raj trapaceou!'
        elif r == 'Spock': res = 'Bazinga!'
        elif r == 'lagarto': res = 'Raj trapaceou!'
    if s == 'pedra':
        if r == 'papel': res = 'Raj trapaceou!'
        elif r == 'pedra': res = 'De novo!'
        elif r == 'tesoura': res = 'Bazinga!'
        elif r == 'Spock': res = 'Raj trapaceou!'
        elif r == 'lagarto': res = 'Bazinga!'
    if s == 'tesoura':
        if r == 'papel': res = 'Bazinga!'
        elif r == 'pedra': res = 'Raj trapaceou!'
        elif r == 'tesoura': res = 'De novo!'
        elif r == 'Spock': res = 'Raj trapaceou!'
        elif r == 'lagarto': res = 'Bazinga!'
    if s == 'lagarto':
        if r == 'papel': res = 'Bazinga!'
        elif r == 'pedra': res = 'Raj trapaceou!'
        elif r == 'tesoura': res = 'Raj trapaceou!'
        elif r == 'Spock': res = 'Bazinga!'
        elif r == 'lagarto': res = 'De novo!'
    if s == 'Spock':
        if r == 'papel': res = 'Raj trapaceou!'
        elif r == 'pedra': res = 'Bazinga!'
        elif r == 'tesoura': res = 'Bazinga!'
        elif r == 'Spock': res = 'De novo!'
        elif r == 'lagarto': res = 'Raj trapaceou!'
    
    print(f'Caso #{(i+1)}: {res}')
