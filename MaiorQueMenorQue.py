from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Maior Que Menor Que'))
print('')

sleep(2)

maior = 0
menor = 0
for c in range(1, 4):
    n = int(input('Digite o {}º número: '.format(c)))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('O maior número lido foi de {}'.format(maior))
print('O menor número lido foi de {}'.format(menor))