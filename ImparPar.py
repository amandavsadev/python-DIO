# Função do Programa: Dizer se o número digitado é ímpar ou par.
# Autora: Amanda Amorim.

a = int(input('Digite um valor: '))
resto = a % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é ímpar')

print('fim do programa')
