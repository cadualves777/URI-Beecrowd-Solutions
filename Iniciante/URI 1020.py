idade = int(input())

ano = idade // 365
r_ano = idade % 365

mes = r_ano // 30
dia = r_ano % 30

print(f"""{ano} ano(s)
{mes} mes(es)
{dia} dia(s)""")
