from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Contagem Regressiva'))
print('')

sleep(2)

for n in range(10, 0, -1):
    print(n)
    sleep(0.5)

print('FIM')

