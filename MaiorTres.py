# Função do programa: Mostra qual dos 3 números é maior.
# Autora: Amanda Amorim

a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro valor: '))

# Condicional if(se) e operador lógico and
if a > b and a > c:
    print('O maior valor é {}'.format(a))
# em python, conseguimos definir o início e o fim de um bloco através da identação.

# else if
elif b > a and b > c:
    print('O maior número é {}'.format(b))

else:
    print('O maior número é {}'.format(c))

print('final do programa')
