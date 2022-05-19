# Função do programa: Saber se 3 números digitados são iguais ou diferentes.
# Autora: Amanda Amorim.

print('Digite 3 números e saiba se:')
print('1 - Todos os números são iguais;')
print('2 - Todos os números são diferentes;')
print('3 - Apenas dois números são iguais.\n')

n1 = int(input('Primeiro número: \n'))
n2 = int(input('Segundo número: \n'))
n3 = int(input('Terceiro número: \n'))

if (n1 == n2) and (n2 == n3):
    print('\n1 - Todos os números são iguais\n')

elif (n1 != n2) and (n2 != n3):
    print('\n2 - Todos os números são diferentes;\n')

else:
    print('\n3 - Apenas dois números são iguais.\n')

print('Fim do programa.')
