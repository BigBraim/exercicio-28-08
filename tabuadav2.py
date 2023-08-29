from time import sleep
print('')
print('-='*18)
print('''Olá 
Seja Bem-Vindo ao código do Brayan''')
print('-='*18)
print('{:^35}'.format('Tabuada V2.0'))
print('')

sleep(2)

continua = 'S'

while continua == 'S':

    operacao = input("Digite / para dividir ou x para multiplicar (digite back para voltar): ")
    match operacao:
        case "/":

            def tabuadadivis (numero):
                for i in range(1, 11):
                    quociente = numero / i

                    print('{} / {} = {:.2f}'.format(numero,i,quociente))

            try:
                numero = int(input("Tabuada de divisão do número: "))
                tabuadadivis(numero)
            except ValueError:
                print("ERRO: Digite apenas números!")

            continua = input('Quer continuar? [S/N] ').upper()



        case "x":
            def tabuadamulti (numero):
                for i in range(1, 11):
                    quociente = numero * i
                    print(f"{numero} x {i} = {quociente}")


            try:
                numero = int(input("Tabuada de multiplicação do número: "))
                tabuadamulti(numero)
            except ValueError:
                print("ERRO: Digite apenas números!")

            continua = input('Quer continuar? [S/N] ').upper()