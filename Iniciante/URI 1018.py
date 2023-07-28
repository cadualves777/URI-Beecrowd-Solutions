n = int(input())
cem = n // 100
resto_cem = n % 100

cinq = resto_cem // 50
resto_cinq = resto_cem % 50

vint = resto_cinq // 20
resto_vint = resto_cinq % 20

dez = resto_vint // 10
resto_dez = resto_vint % 10

cinc = resto_dez // 5
resto_cinc = resto_dez % 5

dois = resto_cinc // 2
um = resto_cinc % 2

print(f"""{n}
{cem} nota(s) de R$ 100,00
{cinq} nota(s) de R$ 50,00
{vint} nota(s) de R$ 20,00
{dez} nota(s) de R$ 10,00
{cinc} nota(s) de R$ 5,00
{dois} nota(s) de R$ 2,00
{um} nota(s) de R$ 1,00""")
