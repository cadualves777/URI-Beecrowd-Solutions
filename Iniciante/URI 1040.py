n1, n2, n3, n4 = map(float, input().split())
media = (2*n1 + 3*n2 + 4*n3 + n4) / 10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n_exame = float(input())
    print(f'Nota do exame: {n_exame}')
    media_final = (media + n_exame) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
