""" A confederação nascional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostrea a sua
 categoria conforme a sua idade:
 > até 9 anos: MIRIM
 > Até 14 anos: INFANTIL
 > Até 19 anos: JUNIOR
 > Até 20 anos: SÊNIOR
 >Acima: MASTER
"""
from datetime import date

atual = date.today().year
nome = str(input('Ola, atleta para começar digite seu nome: '))
nascimento = int(input('Certo \33[0;49;92m{}\33[0m, Agora digite o ano de nascimento: '.format(nome)))
idade = atual - nascimento
print('\33[0;49;92m{}\33[0m tem \33[0;49;31m{}\33[0m anos'.format(nome, idade))

if idade <= 9:
    print('Classificação: \33[049;34mMIRÍN\33[0m')
elif idade <= 14:
    print('Classificaçao: \33[049;34mINFÂNTIL\33[0m')
elif idade <= 19:
    print('Classificação: \33[049;34mJUNIOR\33[0m')
elif nascimento <= 25:
    print('Classificação: \33[0;37mSÊNIOR\33[0m')
else:
    print('Classificação: \33[031mMASTER\33[0m')
