# Função do programa: Calcular a média final
# Autor: Amanda Amorim
print('\tMÉDIA FINAL\t\n')

# Entrada da nota do primeiro bimestre
n1 = int(input('Nota do primeiro bimestre: '))
while n1 > 10:
    n1 = int(input('Nota inválida! Primeiro bimestre: '))

# Entrada da nota do segundo bimestre
n2 = int(input('Nota do segundo bimestre: '))
while n2 > 10:
    n2 = int(input('Nota inválida! Segundo bimestre: '))

# Entrada da nota do terceiro bimestre
n3 = int(input('Nota do terceiro bimestre: '))
while n3 > 10:
    n3 = int(input('Nota inválida! Terceiro bimestre: '))

# Entrada da nota do quarto bimestre
n4 = int(input('Nota do quarto bimestre: '))
while n4 > 10:
    n4 = int(input('Nota inválida! Quarto bimestre: '))

# Calculo da média
media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print('\nMédia: {}'.format(media))
    print('Situação: Aprovado!')

elif 7 > media and media >= 4:
    print('\nMédia: {}'.format(media))
    print('Situação: Recuperação')

else:
    print('\nMédia: {}'.format(media))
    print('Situação: Reprovado')
