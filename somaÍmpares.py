from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Soma Ímpares'))
print('')

sleep(2)

soma = 0

for v in range(0+1, 16, 2):
    soma += v
    print(v)
    sleep(0.5)

print('')
print('Soma dos números ímpares é: {} '.format(soma))
print('FIM')