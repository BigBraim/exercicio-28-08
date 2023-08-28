from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Contagem de Pares'))
print('')

sleep(2)

for v in range(0, 16+1, 2):
    print(v)
    sleep(0.5)

print('FIM')