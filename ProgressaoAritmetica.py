from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Progressão Aritmética'))
print('')

sleep(2)

termo1 = int(input('Digite um número: '))
pule = int(input('Digite de quantos em quantos números vc quer pular: '))
print('')
termo2 = termo1 + (10 - 1) * pule

for v in range(termo1, termo2 + pule, pule):
    print('{} '.format(v), end='-> ')
    sleep(0.5)

print('FIM')